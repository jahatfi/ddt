"""
Defines a decorator and helper functions that together
can create unit tests for decorated functions by hooking the
decorated function during execution.

Any function wrapped with this decorator will have
its execution coverage saved as though under a unit test.
Additionally, all the following will be saved:
1. All accessed global variables (both read from and written to)
2. The arguments to the function, both args and kwargs
3. The result of the function

Execution coverage (set of line numbers executed) of
each invocation will be tracked and aggregated to the
union of coverage of all previous executions.

This wrapper will
deactivate and simply return the results of the function, once
desired coverage is achieved, ceasing to
track any further coverage and removing the overhead involved in such
monitoring.
"""
import copy
import dataclasses
import hashlib
import inspect
import json
import logging
import os
import pprint
import re
import subprocess
import sys
import time
import types
import typing
from collections import defaultdict
from dataclasses import dataclass
from dis import dis
from functools import wraps
from io import StringIO
from json import JSONEncoder

# NOTE: WindowsPath is in fact required if running on Windows!
from pathlib import Path, WindowsPath  # noqa: F401 # pylint: disable=unused-import
from subprocess import CalledProcessError
from types import MappingProxyType
from typing import List, Optional, ParamSpec, Callable, TypeVar, Set

import coverage
import pandas as pd
from pandas import DataFrame

Param = ParamSpec("Param")
# pylint: disable-next=invalid-name
RetType = TypeVar("RetType")

# pylint: disable-next=fixme
# TODO Import any modules here for whom 'repr' doesn't work,
# Then redefine the repr function (see further below, search "repr")

pp = pprint.PrettyPrinter(indent=3)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

recursion_depth_per_decoratee: dict[str, int] = defaultdict(int)

def fullname(o:object):
    """
    Return the "Fully Qualified Name (FQN) of a provided Python
    object. Copied on 21 jAN 2024 directly from Greg Bacon's answer on
    https://stackoverflow.com/questions/2020014/
    """
    module = o.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return o.__class__.__name__
    return module + '.' + o.__class__.__name__
class Jsonable:  # pylint: disable=too-few-public-methods
    """
    Classes that inherit from this one inherit the toJSON(),
    easily creating a string representation of the class.
    """
    def toJSON(self): # pylint: disable=invalid-name
        """
        Return this class representated as its runtime dictionary
        """
        return self.__dict__

class JsonableEncoder(json.JSONEncoder):
    """
    Unclear how if at all this is used
    """
    def default(self, o):
        """
        Unclear how if at all this is used
        """
        logger.debug("obj=%s", o)
        if isinstance(o, set):
            return sorted(list(o))
        #if isinstance(obj, type):
        #    return
        return super().default(o)

# https://pynative.com/make-python-class-json-serializable/
class FunctionMetaDataEncoder(JSONEncoder):
    """
    Helper class to encode the FunctionMetaData class as a string by
    returning this object as a dictionary if possible
    """
    def default(self, o)->typing.Any:
        if isinstance(o, set):
            return sorted(list(o))
        if isinstance(o, MappingProxyType):
            logger.warning("Skipping encoding of %s, it's a Mapping ProxyType", o)
        else:
            try:
                return o.__dict__
            except AttributeError as e:
                logger.warning("%s for %s", e, o)
        return None

def _default(obj):
    """
    Helper class to encode the FunctionMetaData class as a string by
    returning this object as a dictionary if possible
    """
    if isinstance(obj, set):
        return sorted(list(obj))
    try:
        iterable = iter(obj)
    except TypeError as e:
        raise  e
    return list(iterable)
    #return json.JSONEncoder.default(obj)

@dataclass
# pylint: disable-next=too-many-instance-attributes
class CoverageInfo:
    """
    Holds all data gathered from recording/hooking a function/method call
    """
    args: list[str] = dataclasses.field(default_factory=list)
    kwargs: dict[str, typing.Any] = dataclasses.field(default_factory=dict)
    globals_before: dict[str, typing.Any] = dataclasses.field(default_factory=dict)
    globals_after: dict[str, typing.Any] = dataclasses.field(default_factory=dict)
    expected_result: str  = ""
    expected_type: str = ""
    coverage: list[int] = dataclasses.field(default_factory=list)
    exception_type: str = ""
    exception_message: str = ""
    constructor: str = ""
    cost:float = 0.0

    def repr(self):
        """
        This function represents  CoverageInfo as a string that
        is valid Python code.  This string can be used to re-create
        the object in Python.
        """
        result = ["CoverageInfo(args="+repr(self.args)]
        result.append(" kwargs="+repr(self.kwargs))
        result.append(" globals_before="+repr(self.globals_before))
        result.append(" globals_after="+repr(self.globals_after))
        result.append(" expected_result="+repr(self.expected_result))
        result.append(" expected_type="+repr(self.expected_type))
        result.append(" coverage="+repr(self.coverage))
        result.append(" exception_type="+repr(self.exception_type))
        result.append(" exception_message="+repr(self.exception_message))
        result.append(" constructor="+repr(self.constructor).replace('\"', "\""))
        result.append(" cost="+repr(self.cost)+')')

        result = ','.join(result)
        logger.debug("result=%s", result)
        return result

    def __repr__(self) -> str:
        """
        This function represents FunctionMetaData as a string that
        is valid Python code.  This string can be used to re-create
        the object in Python.
        """
        return self.repr()

    def __str__(self) -> str:
        """
        This function represents  CoverageInfo as a string that
        is valid Python code.  This string can be used to re-create
        the object in Python.
        """
        result = ["CoverageInfo(args="+repr(self.args)]
        result.append(" kwargs="+repr(self.kwargs))
        result.append(" globals_before="+repr(self.globals_before))
        result.append(" globals_after="+repr(self.globals_after))
        result.append(" expected_result="+repr(self.expected_result))
        result.append(" expected_type="+repr(self.expected_type))
        result.append(" coverage="+repr(self.coverage))
        result.append(" exception_type="+repr(self.exception_type))
        result.append(" exception_message="+repr(self.exception_message))
        result.append(" constructor="+repr(self.constructor).replace('"', "\"")+")")

        result_str = ','.join(result)
        logger.debug("result=%s", result_str)
        return result_str

# pylint: disable-next=too-many-instance-attributes
class FunctionMetaData(Jsonable):
    """
    Class to track metadata when testing functions and methods
    """
    # pylint: disable-next=too-many-arguments
    def __init__(   self,
                    name:str,
                    parameter_names:List[str],
                    is_method:bool,
                    source_file:Path,
                    lines:Optional[List[int]] = None,
                    global_vars_read_from:Optional[set] = None,
                    global_vars_written_to:Optional[set] = None,
                    coverage_io:Optional[dict] = None,
                    coverage_percentage:float=0.0,
                    types_in_use:Optional[set] = None,
                    unified_test_coverage:Optional[set] = None,
                    needs_pytest:bool = False,
                    exceptions_raised:Optional[set] = None
                ):
        # These properties (expect non_lines) are always provided
        self.name = name
        self.parameter_names = parameter_names
        self.is_method = is_method
        self.source_file = source_file
        # This one is not provided, but infered later
        self.non_code_lines:set = set()
        # These properties are not provided unless this class
        # is being constructed as part of a unit test
        self.coverage_io = {} if coverage_io is None else coverage_io
        self.coverage_percentage = coverage_percentage
        self.types_in_use = set() if types_in_use is None else types_in_use

        # Change in style simply to keep line length below 80 characters
        if lines is None:
            self.lines = []

        else:
            self.lines = lines
            self.non_code_lines = self.return_non_code_lines()

        if global_vars_read_from is None:
            self.global_vars_read_from = set()
        else:
            self.global_vars_read_from = global_vars_read_from

        if global_vars_written_to is None:
            self.global_vars_written_to = set()
        else:
            self.global_vars_written_to = global_vars_written_to

        if unified_test_coverage is None:
            self.unified_test_coverage = set()
        else:
            self.unified_test_coverage = unified_test_coverage

        self.needs_pytest = needs_pytest

        if exceptions_raised is None:
            self.exceptions_raised = set()
        else:
            self.exceptions_raised = exceptions_raised

    def update_lines(self, lines: List[int]):
        """
        Assigns the provided List of ints (line numbers) to "lines"
        property of this class.
        Also updates the non_code_lines
        """
        self.lines = lines
        self.non_code_lines = self.return_non_code_lines()

    def percent_covered(self, precision:int=2):
        """
        Compute and return percent of covered lines,
        rounded to 'precision' digits.
        """
        self.unified_test_coverage = set(self.lines) & self.unified_test_coverage
        pct = len(self.unified_test_coverage)/len(self.lines)
        pct = round(100*pct, precision)
        return pct

    def get_all_uncovered_line_str(self):
        """
        Return a string representing the uncovered lines
        All those lines not covered by ANY of the tests
        """
        uncovered = set(self.lines)
        for _, record in self.coverage_io.items():
            uncovered -= set(record.coverage)
        logger.debug("uncovered=%s self.non_code_lines=%s",
                     uncovered, self.non_code_lines)
        if uncovered:
            result = coverage_str_helper(list(uncovered), self.non_code_lines)
        else:
            result = uncovered
        logger.debug("result=%s", result)
        return result


    def __str__(self):
        return f"{self.name}:\n{self.lines=}\n"

    def return_non_code_lines(self)->Set[int]:
        """
        Return a set of the line numbers of this function that are NOT
        code, e.g. whitespace or comments.
        """
        if not self.lines:
            return set()
        first_source_line_num = self.lines[0]
        last_source_line_num = self.lines[-1]
        range_source_line_nums =   set(range(first_source_line_num,
                                                        last_source_line_num+1))

        non_code_lines = range_source_line_nums - set(self.lines)
        return non_code_lines

    def repr(self)->str:
        """
        This function represents FunctionMetaData as a string that
        is valid Python code.  This string can be used to re-create
        the object in Python.
        """
        result = [f"FunctionMetaData(name=\'{self.name}\'"]

        result.append(" lines="+repr(self.lines))
        result.append(" parameter_names="+repr(self.parameter_names))
        result.append(" is_method="+repr(self.is_method))
        result.append(" global_vars_read_from="+repr(self.global_vars_read_from))
        result.append(" global_vars_written_to="+repr(self.global_vars_written_to))
        result.append(" source_file="+repr(self.source_file))
        result.append(" coverage_io="+repr(self.coverage_io))
        result.append(" coverage_percentage="+repr(self.coverage_percentage))
        result.append(" types_in_use="+repr(self.types_in_use))
        result.append(" unified_test_coverage="+repr(self.unified_test_coverage))
        result.append(" needs_pytest="+repr(self.needs_pytest)+')')
        result_str = ','.join(result)
        logger.debug("result=%s", result_str)
        return result_str

    def __repr__(self) -> str:
        """
        This function represents FunctionMetaData as a string that
        is valid Python code.  This string can be used to re-create
        the object in Python.
        """
        return self.repr()

    def purge_record(self, hash_key):
        """
        Delete IO record with this hashed_input as key
        NOTE: Need to add "update_types_in_use" method and convert
        types_in_use to a dict {hash_key:set(types_per_hash_key)}
        if this function is ever called.
        """
        update_fields = [self.coverage_io]
        for field in update_fields:
            try:
                field.pop(hash_key)
            except KeyError as e:
                # NOTE: Fix the root cause of this bug
                logger.error("Failed to pop key: %s", e)
        # NOTE: call self.update_types_in_use here?

    def default(self):
        """Wrapper for _default() method"""
        return _default(self)

    # https://stackoverflow.com/questions/3768895
    def to_json(self):
        """
        Convert this class to a json-string
        """
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

# https://stackoverflow.com/questions/47060133/python-3-type-hinting-for-decorator
def unit_test_generator_decorator(  percent_coverage: Optional[int]=0,
                                    sample_count: Optional[int]=0,
                                    keep_subsets: bool=False)->Callable[[Callable[Param, RetType]],
                                                                         Callable[Param, RetType]]:
    """
    Decorate a function F by recording inputs and outputs during execution such
    that a call to generate_all_tests_and_metadata() can use those recorded
    inputs and outputs to programmatically generate unit tests for F.
    This adds a lot of time and computation in overhead.

    NOTE: For complex functions the Law of Diminishing Returns likely
    applies, meaning that more and more executions of a function will likely
    be required to cover marginally more lines/branches.  Hence, once ~80%
    code coverage is hit it may be desirable to cease logging of inputs and
    outs to reduce overhead.

    The caller MUST specify exactly one of the following metrics to
    determine when, if at all, to cease the logging of inputs/outputs and
    reduce the overhead (but no longer achieve new code coverage in the
    subsequently created unit test):
    1. percent_coverage: 80 is a recommended starting value for
    complex functions, but 100 may be achievable for trivial functions.
    Any value over 100 will record ALL executions.
    2. sample_count: Record the inputs and output of N unique calls to this
    function, then stop recording them.
    3. If neither of the above are specified, the decorator will NOT be applied.
    """
    @wraps(unit_test_generator_decorator)
    def actual_decorator(func:Callable)->Callable[Param, RetType]:
        """
        Any function wrapped with this decorator will have
        its execution coverage saved as though under a unit test.
        Additionally, all the following will be saved:
        1. All accessed global variables (both read from and written to)
        2. The arguments to the function, both args and kwargs
        3. The result of the function

        Execution coverage (set of line numbers executed) of
        each invocation will be tracked and aggregated to the
        union of coverage of all previous executions.

        This wrapper will
        deactivate when desired coverage is achieved,
        and simply return the results of the function, ceasing to
        track any further coverage and removing the overhead involved in such
        monitoring.

        When main() completes, main() writes out the coverage results to one file
        per decorated function.
        """
        @wraps(func)
        # pylint: disable-next=too-many-return-statements
        def unit_test_generator_decorator_inner(*args, **kwargs)->RetType:
            """
            Immediately return function results if:
            1. no stop parameter is specified.
            2. func is being called in a cycle, e.g. A->B->A.
            Get or create the metadata for this class.  Immediately return
            function results if desired coverage/samples already met, else
            apply the decorator to func.
            """
            function_name = str(func).split()[1]
            if percent_coverage == 0 and sample_count == 0:
                # To decorate a function with this decorator,
                # the user MUST specify at least one of these values.
                # If none are specified, simply call the function and
                # immediately return the result,
                # i.e. this decorator has no effect.
                logger.debug("percent_coverage & sample_count == 0 %s; skip decorator",
                             function_name)
                # Since this decorator is effectively nullified, do NOT
                # try/catch/raise any exceptions.
                result = func(*args, **kwargs)
                return result

            # pylint: disable-next=global-variable-not-assigned
            global recursion_depth_per_decoratee
            if "pytest" in sys.modules:
                logger.debug("pytest is loaded; don't decorate when under a test")
                result = func(*args, **kwargs)
                return result

            function_calls: dict[str, int] = defaultdict(int)

            # The code blocks below (before the call to do_the_decorator_thing)
            # prevent application of this decorator in cyclical calls, e.g.
            # A -> B -> A # Does not apply to decorator in 2nd call to A
            for f in inspect.stack()[::-1]:
                this_frame = inspect.getframeinfo(f[0])
                function_calls[this_frame.function] += 1

            max_func_call_vals = max(function_calls.values())
            if function_name not in recursion_depth_per_decoratee:
                recursion_depth_per_decoratee[function_name] = max_func_call_vals

            elif 1 < max_func_call_vals >= recursion_depth_per_decoratee[function_name]:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.critical(e)
                    raise e
            try:
                # At this point we know we aren't in a function call graph
                # cycle.  Gather some more info to determine if we want to
                # apply the decorator
                if not function_name:
                    # Parsing error, skip this decorator.
                    logger.warning("function_name is Falsey; skip decorator")
                    # Since this decorator is effectively nullified now,
                    # do NOT try/catch/raise any exceptions.
                    return func(*args, **kwargs)
                this_metadata: FunctionMetaData = None # type: ignore[assignment]
                source_file = Path(func.__code__.co_filename).absolute()

                # If this is the first time this func has been called,
                # disassemble it to get the lines and global variables
                if function_name not in all_metadata:
                    # Using single var names ('x', 'y') to keep lines short
                    parameters = inspect.getfullargspec(func)[0]
                    this_metadata = FunctionMetaData(   name=function_name,
                                                        parameter_names=parameters,
                                                        is_method='.' in function_name,
                                                        source_file=source_file
                                                    )
                    update_metadata(func, this_metadata)

                else:
                    this_metadata = all_metadata[function_name]

                # Check if this decorator should be applied based on the
                # provided percent_coverage or sample_count variables
                if percent_coverage and percent_coverage <= this_metadata.percent_covered(0):
                    # Desired percent coverage already achieved: skip
                    logger.info("%d coverage for %s already achieved: skip decorator",
                                percent_coverage, function_name)
                    # Since this decorator is effectively nullified now,
                    # do NOT try/catch/raise any exceptions.
                    return func(*args, **kwargs)

                if sample_count and sample_count <= len(this_metadata.coverage_io):
                    # Desired number of samples already achieved: skip
                    logger.info("%d samples for %s already collected: skip decorator",
                                sample_count, function_name)
                    logger.info(this_metadata.coverage_io)
                    # Since this decorator is effectively nullified now,
                    # do NOT try/catch/raise any exceptions.
                    return func(*args, **kwargs)

                # percent_coverage or saple_count properly specified, but
                # desired coverage/samples not yet achieved
                # so apply the decorator
                logger.info("Decorate %s", function_name)
                return do_the_decorator_thing(func, function_name, this_metadata,
                                              str(source_file), keep_subsets,
                                              *args, **kwargs)
            except Exception as e:
                logger.warning("e=%s", e)
                raise e
        return unit_test_generator_decorator_inner
    return actual_decorator

def _pandas_df_repr(df: pd.DataFrame)->str:
    '''
    Sadly, the 'repr' method for Pandas DataFrames does not work the
    same as 'repr' for built-in types.  Specifically, while 'repr' on
    built-in types (strings, lists, dicts, etc) produces valid Python
    code that can be instantly used to re-create the original object,
    this is not true of Pandas DataFrames, which are instead pretty
    printed as a table.  The best alternative for non-empty dataframes is
    https://stackoverflow.com/questions/67845199 by user Silveri
    Overwrite the native Pandas DataFram repr() method with that approach.
    '''
    return f"DataFrame.from_dict({df.to_dict()})"

pd.DataFrame.__repr__ = _pandas_df_repr # type: ignore[method-assign, assignment]

def get_module_import_string(my_path:Path)->str:
    """
    Given a module, return a dotted import string, the
    fully qualified name to that module, e.g.
    "package.module"
    """

    files = set(sorted(sys.path))
    keep_file = None
    this_type = ""
    for file_str in files:
        file = Path(file_str)
        if my_path.is_relative_to(file):
            keep_file = file
            logger.debug("os.path.relpath(file, my_path, )=%s",
                         os.path.relpath(file, my_path, ))
            this_type = f"{os.path.relpath(file, my_path)}"
    if keep_file:
        my_path_str = str(my_path)[len(str(keep_file)):]
        my_path_str = re.sub(r"^[\\/]", "", my_path_str)
        this_type = re.sub(".py$", "", my_path_str)
        if not this_type:
            raise TypeError("Can't determine type")
        this_type = re.sub(r"\\", ".", this_type)

        # Other other OS's use forward slashes
        this_type = re.sub(r"/", ".", this_type)

    return this_type

def get_class_import_string(arg:typing.Any):
    """
    Given a class, return a dotted import string, the
    fully qualified name to that class, e.g.
    "package.module.class"
    """

    my_path = Path(inspect.getabsfile(arg.__class__))
    files = set(sorted(sys.path))
    keep_file = None
    this_type = ""
    for file in files:
        file_path = Path(file)
        if my_path.is_relative_to(file_path):
            keep_file = file_path
            this_type = f"{os.path.relpath(file_path, my_path)}"
    if keep_file:
        my_path_str = str(my_path)[len(str(keep_file)):]
        my_path_str = re.sub(r"^[\\/]", "", my_path_str)
        this_type = f'{re.sub(".py$", "", my_path_str)}.{arg.__class__.__qualname__}'
        this_type = re.sub(r"\\", ".", this_type)
        # Other other OS's use forward slashes
        this_type = re.sub(r"/", ".", this_type)

    return this_type

def get_method_class_import_string(arg:typing.Any):
    """
    Given a method, return a dotted import string, the
    fully qualified name to its class, e.g.
    "package.module.class"
    """
    my_path = Path(inspect.getabsfile(arg))
    files = set(sorted(sys.path))
    keep_file = None
    this_type = ""
    for file_str in files:
        file = Path(file_str)
        if my_path.is_relative_to(file):
            keep_file = file
            this_type = f"{os.path.relpath(file, my_path)}"
    if keep_file:
        my_path_str = str(my_path)[len(str(keep_file)):]
        my_path_str = re.sub(r"^[\\/]", "", my_path_str)
        this_type = re.sub(".py$", "", my_path_str) + "." + arg.__name__
        this_type = re.sub(r"\\", ".", this_type)
        # Other other OS's use forward slashes
        this_type = re.sub(r"/", ".", this_type)

    return this_type

@unit_test_generator_decorator(percent_coverage=0, sample_count=1)
def sorted_set_repr(obj: set):
    """
    I want sets to appear sorted when initialized in unit tests.
    Thus function does just that.
    """
    obj_list = sorted(list(obj))
    # 2. Convert the list to valid Python code
    obj_list_repr = repr(obj_list)
    # Replace the square brackets (list) to curly braces (set)
    obj_set_code = f"{{{obj_list_repr[1:-1]}}}"
    # "obj" is now valid Python code that will create a set.
    # The objects in this line of code appear in sorted order
    return repr(obj_set_code)


pp = pprint.PrettyPrinter(indent=3)

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

def get_filename(arg:str):
    """
    Returns the name of this Python module if valid,
    else returns the empty string.
    """
    file_name = ""
    file_name_match = re.search(r"([\w]+).py", arg)
    if file_name_match:
        file_name = str(file_name_match.groups()[0])
    return file_name

# pylint: disable-next=too-many-locals,too-many-statements,too-many-branches
def do_the_decorator_thing(func: Callable, function_name:str,
                           this_metadata:FunctionMetaData, source_file: str,
                           keep_subsets:bool, *args, **kwargs):
    """
    Any function wrapped with this decorator will have
    its execution coverage saved as though under a unit test.
    Additionally, all the following will be saved:
    1. All accessed global variables (both read from and written to)
    2. The arguments to the function, both args and kwargs
    3. The result of the function

    Execution coverage (set of line numbers executed) of
    each invocation will be tracked and aggregated to the
    union of coverage of all previous executions.

    This wrapper will
    deactivate and simply return the results of the function, once
    desired coverage is achieved, ceasing to
    track any further coverage and removing the overhead involved in such
    monitoring.

    When main() completes, main() writes out the coverage results to one file
    per decorated function.
    """
    # pylint: disable-next=global-variable-not-assigned
    global all_metadata, hashed_inputs
    caught_exception = None
    kwargs = kwargs.get("kwargs", kwargs)
    #if 'kwargs' in kwargs:
    #    kwargs = kwargs['kwargs']

    #logger.critical(f"Decorating {function_name}".center(80, '-'))


    #if function_name in all_metadata and\
    #    all_metadata[function_name].coverage_percentage >= coverage_cutoff:
    #    logger.debug(f"Hit >={coverage_cutoff=} in {function_name}; skip it.")
    #    x = func(*args, **kwargs)
    #    #logger.critical(f"Undecorating {function_name}".center(80, '-'))
    #    return x

    if "pytest" in sys.modules:
        logger.debug("pytest is loaded; don't decorate when under a test")
        result = func(*args, **kwargs)
        logger.debug(f"Undecorating {function_name}".center(80, '-'))
        return result

    this_coverage_info: CoverageInfo = CoverageInfo()

    #args_copy = [convert_to_serializable(x) for x in args]
    args_copy:list[str] = []
    class_type = None
    if this_metadata.is_method:
        if not function_name.endswith("__init__"):
            logger.info("Found non-constructor method: %s %s", function_name, args[0])
            this_coverage_info.constructor = args[0].repr()
            logger.info(args)
            this_type = get_class_import_string(args[0])
            class_type = copy.deepcopy(this_type)
        else:
            logger.critical("Found Constructor: %s args=%s", function_name, args[1:])


    new_types_in_use = set()

    for arg_i, arg in enumerate(args):
        # Do not include the first arg of a method (it's "self")
        # in the argument list
        if this_metadata.is_method and arg_i == 0:
            continue
        if (
                callable(arg) and inspect.isfunction(arg) and
                "." in arg.__qualname__ and arg.__qualname__[0].isupper()
            ):
            newest_import_list = f"{arg.__module__}.{arg.__qualname__}".split('.')
            newest_import = '.'.join(newest_import_list[:-1])
            args_copy.append(arg.__qualname__)
            # Reset the class type, as this newest_import will be used instead
            class_type = None
            if arg.__module__ == "__main__":
                file_name = get_filename(str(arg.__code__))
                if file_name:
                    newest_import = re.sub("__main__", file_name, newest_import)
                else:
                    logger.critical("NO FILENAME FOUND!: %s",
                                    re.escape(str(arg.__code__)))
            new_types_in_use.add(newest_import)

            continue

        new_types_in_use |= get_all_types("1", arg, False, 0, function_name)
        if hasattr(arg, "__dict__"):
            logger.info("Adding types for function %s for arg %s", function_name, arg)
            for v in arg.__dict__.values():
                new_types_in_use |= get_all_types("1.1", v, False, 0, function_name)
        if callable(arg):
            logger.critical('callable')
            if arg.__module__ == "__main__":
                file_name = get_filename(str(arg.__code__))
                if file_name:
                    logger.critical("%s.%s",file_name, arg.__name__)
                    args_copy.append(f"{file_name}.{arg.__name__}")
                else:
                    logger.critical("NO FILENAME FOUND!: %s",
                                    re.escape(str(arg.__code__)))
            else:
                args_copy.append(arg.__qualname__)

            #sys.exit(1)
        elif not isinstance(arg, str):
            type_str = str(type(arg))
            #logger.critical(arg)
            logger.debug("type_str=%s %s", type_str, type(arg).__module__)

            # Reference for line:
            # 'type(arg).__module__ != "__builtin__":'
            # https://stackoverflow.com/questions/46876484/
            # Answer by user moar10
            if bool(re.match(r"<class[^\.]+\.", type_str)) and\
                type(arg).__module__ != "__builtin__":
                class_repr = repr(arg)
                if "object at 0x" in class_repr:
                    class_repr = arg.repr()
                try:
                    logger.info(class_repr)
                    # This eval is necessary to check if classes can in fact
                    # be represented as strings.  If not, and this SyntaxError
                    # is uncaught, it will break everything.
                    # pylint: disable-next=eval-used
                    eval(class_repr)
                    args_copy.append(class_repr)

                except SyntaxError as e:
                    try:
                        class_repr = arg.repr()
                        logger.debug("%s, class_repr = %s", e, class_repr)
                    except AttributeError as e2:
                        # skip on error
                        logger.error("\"%s\" raised %s decorating %s repr'ing arg=%s:\ne=%s\n%s",
                                    class_repr, type(e2), function_name, arg, e2, arg)
                        logger.error(arg.__repr__)
                        all_metadata[function_name] = this_metadata
                        return func(*args, **kwargs)

                except NameError as e:
                    # What's going on here?
                    # This argument (arg) is a class, but that class hasn't
                    # been imported, so calling "eval" on
                    # it yielded a NameError.  No problem, assume that we
                    # can import it later; now we simply record it as one of
                    # the arguments to this decoratee by adding it to args_copy.
                    logger.debug(e)
                    logger.critical("%s: class_repr=%s arg=%s",
                                    function_name, class_repr, arg)
                    #this_coverage_info.constructor = copy.deepcopy(class_repr)

                    args_copy.append(class_repr)
            else:
                args_copy.append(repr(arg))
        else:
            args_copy.append("\""+re.sub(r'(?<!\\)\"', r'\\"',arg)+"\"")

    if class_type:
        this_metadata.types_in_use.add(class_type)

    this_metadata.types_in_use |= new_types_in_use
    this_coverage_info.args = args_copy

    phase = "Before"
    # Record the values of any global variables READ BY this function
    for this_global in this_metadata.global_vars_read_from:
        obj = func.__globals__[this_global]
        this_coverage_info = update_global(obj, this_global, phase, this_coverage_info)
        these_types = get_all_types("2", func.__globals__[this_global], True, 0, function_name)
        this_metadata.types_in_use |= these_types
    # Also record globals variables WRITTEN TO by the function, as we may
    # need to know their values in order to assert the "After"
    # values are correct once the function executes.
    # (E.g. if the function appends to a previously populated list)
    for this_global in this_metadata.global_vars_written_to:
        obj = func.__globals__[this_global]
        this_coverage_info = update_global(obj, this_global, phase, this_coverage_info)
        these_types = get_all_types("3", func.__globals__[this_global], True, 0, function_name)
        this_metadata.types_in_use |= these_types

    hashed_input = ""

    if kwargs:
        this_coverage_info.kwargs = kwargs

    hashed_input_hash = hashlib.new('sha256')
    hashed_input_hash.update(str(this_coverage_info.globals_before).encode())
    hashed_input_hash.update(str(this_coverage_info.args).encode())
    hashed_input_hash.update(str(this_coverage_info.kwargs).encode())
    hashed_input = hashed_input_hash.hexdigest()

    if hashed_input in hashed_inputs:
        # If this input has already been captured, there's no need to
        # run it again with coverage, just run it and immediately return
        # the result/raise the exception as applicable.
        try:
            if kwargs:
                result = func(*args, **kwargs)
            else:
                start_time = time.perf_counter()
                result = func(*args)
            return result
        except Exception as e:
            raise e

    start_time = 0.0
    end_time = 0.0
    cov_report_ = None
    result = None
    data_file = f"coverage_{function_name}_{time.perf_counter()}"
    cov = coverage.Coverage(data_file)
    with cov.collect():
        try:
            if kwargs:
                this_coverage_info.kwargs = kwargs
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
            else:
                start_time = time.perf_counter()
                result = func(*args)

            logger.debug("No exception :)")
        # There's no way to know ahead of time what kind of exception func
        # might raise, so catch any of them.
        # pylint: disable-next=broad-exception-caught
        except Exception as e:
            #this_metadata.exceptions[hash_key] = e
            logger.critical("function: '%s' Caught %s e=%s", function_name, type(e), e)
            logger.debug("caught_exception=%s @ %s result=%s",
                     caught_exception, hashed_input, result)
            caught_exception = e
            #raise caught_exception'
        finally:
            end_time = time.perf_counter()
    with Capturing() as stdout_lines:
        cov.json_report(outfile='-')
    # result will not exist if the function threw an exception
    cov_report_ = json.loads(stdout_lines[0])
    expected_type = str(type(result))
    parsed_type = re.match("<class '([^']+)'>", expected_type)
    if parsed_type:
        expected_type = parsed_type.groups()[0]

    this_metadata.types_in_use |= get_all_types("4", result, True, 0, function_name)
    #assert hashed_input not in hashed_inputs, "ALREADY"
    this_coverage_info.expected_type = expected_type
    #if hashed_input in this_metadata.coverage_io:
    #    this_metadata.coverage_io[hashed_input].expected_type = expected_type
    #hash_keys.add(hash_keys)

    # There is only one file in cov_report_['files']
    assert len(cov_report_['files']) == 1
    this_coverage = set(cov_report_['files'].popitem()[1]['executed_lines'])
    assert this_coverage & set(this_metadata.lines)
    #logger.critical("this_coverage=%s", this_coverage)
    is_subset = False
    Path.unlink(Path(data_file))

    # If no new lines were covered, do nothing else,
    # but just immediately return the result

    pct_covered = this_metadata.percent_covered()
    pct_covered = round(pct_covered, 4)
    delta = len(this_coverage-this_metadata.unified_test_coverage)

    if delta == 0 and not keep_subsets:
        all_metadata[function_name] = this_metadata
        logger.debug("No new coverage decorating %s; but not skipping.",
                     function_name)
        if caught_exception:
            logger.critical("Raising %s: %s", type(caught_exception), str(caught_exception))
            raise caught_exception
        return result

    pct_improvement = delta / len(this_metadata.lines)
    pct_improvement = round(100*pct_improvement, 4)

    log_message = f"{function_name=}; {len(this_coverage)=}"
    logger.debug(log_message)
    log_message = f"({pct_covered=}%) ({delta=}) {pct_improvement=}"
    logger.debug(log_message)

    # Keeping the code below as it may better when implementing the
    # minimal set cover problem

    # Deepcopy of keys permits modification of the dictionary in the loop
    tmp_key_list = list(this_metadata.coverage_io.keys())
    key_list = copy.deepcopy(tmp_key_list)
    for key in key_list:
        # The key may have been removed in a previous iteration of this loop
        if key not in this_metadata.coverage_io:
            continue
        print(f"{this_metadata.coverage_io=}")
        prev_coverage = set(this_metadata.coverage_io[key].coverage)
        print(f"{prev_coverage=}")
        # Discard this test if it covered a subset of a previous test
        if this_coverage.issubset(prev_coverage) and not keep_subsets:
            logger.debug("%s: discarding current test.", source_file)
            is_subset = True
            break
        # Discard all previous tests that covered a smaller subset
        # of the lines covered by this test
        if prev_coverage.issubset(this_coverage):
            logger.debug("%s removing subset coverage @ %s.", source_file, key)
            this_metadata.coverage_io.pop(key)


    # Put another way, only keep these results IF the test coverage
    # here is NOT a subset of ANY previous run
    if is_subset:
        all_metadata[function_name] = this_metadata
        if caught_exception:
            logger.critical("Raising %s: %s", type(caught_exception), str(caught_exception))
            raise caught_exception
        logger.debug("%s coverage is a subset this_metadata.coverage_percentage=%s",
                     function_name, this_metadata.coverage_percentage)
        #logger.critical(f"Undecorating {function_name}".center(80, '-'))
        return result

    logger.debug("%s coverage @%s is not a subset", function_name, hashed_input)

    if caught_exception:
        caught_exception_str = str(caught_exception)
        caught_exception_type = str(type(caught_exception))
        logger.critical("Caching %s: %s", caught_exception_type, caught_exception_str)
        logger.debug("caught_exception=%s", caught_exception)
        this_coverage_info.exception_type = caught_exception_type
        this_coverage_info.exception_message = caught_exception_str
        this_metadata.needs_pytest = True
        this_metadata.exceptions_raised.add(caught_exception_type)

    if isinstance(result, DataFrame):
        this_coverage_info.expected_result = f"pd.DataFrame.from_dict({result.to_dict()})"
    elif isinstance(result, str):
        this_coverage_info.expected_result = result
    else:
        if isinstance(result, set) and result:
            this_coverage_info.expected_result = sorted_set_repr(result)
        else:
            this_coverage_info.expected_result = repr(result)

    phase = "After"
    for this_global in this_metadata.global_vars_written_to:
        obj = func.__globals__[this_global]
        this_coverage_info = update_global(obj, this_global,
                                           phase, this_coverage_info)
        these_types = get_all_types("5", func.__globals__[this_global], True, 0, function_name)
        this_metadata.types_in_use |= these_types

    this_metadata.unified_test_coverage |= this_coverage
    percent_covered = this_metadata.percent_covered(2)

    logger.debug("Achieved %.2f%% coverage for %s", percent_covered, function_name)
    sorted_coverage = sorted(list(this_coverage))
    logger.debug("sorted_coverage=%s", sorted_coverage)
    this_coverage_info.coverage = sorted_coverage
    hashed_inputs.add(hashed_input)
    this_metadata.coverage_percentage = percent_covered
    this_metadata.coverage_io[hashed_input] = this_coverage_info
    this_metadata.coverage_io[hashed_input].cost = round(end_time - start_time, 3)

    #print("Cost")

    if caught_exception:
        all_metadata[function_name] = this_metadata
        raise caught_exception
    #logger.critical(f"Undecorating {function_name}".center(80, '-'))

    all_metadata[function_name] = this_metadata
    return result


# pylint: disable-next=line-too-long
all_metadata:defaultdict[str, FunctionMetaData] = defaultdict(FunctionMetaData) # type: ignore[arg-type]
hashed_inputs:set[str] = set() # method-assign

class Capturing(list):
    '''
    Use to capture STDOUT output
    '''
    def __init__(self):
        self._stdout = None
        self._stringio = None

    # Source https://stackoverflow.com/questions/16571150
    # By users kindall and Antti Haapala
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def capture(f):
    """
    Decorator to capture standard output
    from https://stackoverflow.com/questions/33160744
    """
    def captured(*args, **kwargs):
        # setup the environment
        backup = sys.stdout
        try:
            sys.stdout = StringIO()     # capture output
            f(*args, **kwargs)
            out = sys.stdout.getvalue() # release output
        finally:
            sys.stdout.close()  # close the stream
            sys.stdout = backup # restore original stdout
        return out # captured output wrapped in a string
    return captured

# Decorating yields recursion exception
def is_global_var(this_global:str, function_globals:dict, function_name:str):
    """
    Not all global "variables" LOADed are relevant, some are just
    imported modules (e.g. os, sys, re, etc). Given a the name of a
    candidate global variable (i.e. variables LOADed or STOREd via
    LOAD_GLOBAL or STORE_GLOBAL bytecodes) and
    the 'f'unction associated with the candidate, return True if the
    candidate is not a function or module.
    """
    is_variable = False
    if this_global in function_globals and \
        not isinstance(function_globals[this_global], (types.FunctionType, types.ModuleType)):
        is_variable = True
    elif this_global in function_globals and \
    isinstance(function_globals[this_global], types.ModuleType):
        logger.debug("Got import for %s this_global=%s", function_name, this_global)
    return is_variable

@unit_test_generator_decorator(sample_count=1)
def update_metadata(f: Callable, this_metadata: FunctionMetaData):
    """
    Given a function, returns three sets:
    1. a set of the line numbers of this function's source code
    2. all global vars read by the provided function
    3. all global vars written to by the provided function
    """
    if hasattr(f, "__wrapped__"):
        f = f.__wrapped__
    line_numbers = []

    global_vars_read_from = set()
    global_vars_written_to = set()
    dis_ = capture(dis)
    logger.debug("f=%s type(f)=%s", f.__name__, type(f))
    disassembled_function = dis_(f)

    for line in disassembled_function.splitlines():
        if "faster" in f.__name__ or "gas" in f.__name__:
            logger.critical(line)
        line_number_match = re.match(r"\s*([\d]+)[ >]+[\d]+ [A-Z]", line)
        if line_number_match:
            line_number = int(line_number_match.groups()[0])
            line_numbers.append(line_number)
        if "LOAD_GLOBAL" in line:
            this_global = line.split("(")[1].split(")")[0]
            if is_global_var(this_global, f.__globals__, f.__name__):
                global_vars_read_from.add(this_global)
        elif "STORE_GLOBAL" in line:
            this_global = line.split("(")[1].split(")")[0]
            if is_global_var(this_global, f.__globals__, f.__name__):
                global_vars_written_to.add(this_global)
    this_metadata.update_lines(line_numbers[1::])
    this_metadata.global_vars_read_from = global_vars_read_from
    this_metadata.global_vars_written_to = global_vars_written_to
    #return this_metadata

@unit_test_generator_decorator(sample_count=1)
def count_objects(obj: typing.Any):
    """
    Given a Python object, e.g. a number, string, list, list of lists,
    list of dictionaries of sets ...
    Count the total number of objects according to these rules:

    Primitives (number, string) and classes count as one object.

    This function is called recursively on Non-dictionary iterables
    such as (lists, sets, tuples) are passed recursive.

    For dictionaries, each key counts as one object, then this function is
    called recursively on the dictionary values.

    E.g.
    count_objects(5) -> 1               # The number 5 is one object
    count_objects([1,2,3]) -> 3         # There are 3 numbers in one list
    count_objects([1,2,[1,2,3,4]]) -> 6 # There are 6 numbers total
    count_objects(  {'a':{1,2,3},
                     'b':{4}}) -> 6 # There are 2 keys + 4 values in sets
    """
    count = 0
    if isinstance(obj, str):
        count += 1
    elif isinstance(obj, dict):
        for v in obj.values():
            count += 1
            count += count_objects(v)

    # Now handle all other iterables aside from dictionaries
    else:
        try:
            for obj_i in obj:
                count += count_objects(obj_i)
        except TypeError:
            # If the object isn't a str or iterable, treat it as one object
            count += 1
    return count

# pylint: disable=too-many-locals, too-many-branches,too-many-return-statements,too-many-statements
def get_all_types(loc: str,
                  obj,
                  import_modules:bool=True,
                  recursion_depth:int=0,
                  decoratee:str="n/a")->set[str]:
    """
    Return the set of all types contained in this object,
    It might be a list of sets so return {"list", "set"}
    """
    # If primitive type, add an immediately return
    if not obj:
        return set()
    parsed_type_match = re.match("<class '([^']+)'>", str(type(obj)))
    if parsed_type_match:
        expected_type = parsed_type_match.groups()[0]
        if expected_type in ['int', 'bool', 'str', 'float']:
            return set()


    if recursion_depth > 2:
        return set()
    all_types: set[str] = set()
    type_str = str(type(obj))

    parsed_type_match = re.match("<class '([^']+)'>", type_str)
    if parsed_type_match:
        parsed_type:str = parsed_type_match.groups()[0]

    if callable(obj):
        if hasattr(obj, "__code__"):
            logger.debug("%s %s.%s as callable",
                         loc, obj.__module__, obj.__name__)
            file_name = get_filename(str(obj.__code__))
            if file_name:
                if import_modules:
                    logger.debug("Adding %s.%s", file_name, obj.__name__)
                    return set([f"{file_name}.{obj.__name__}"])
                logger.debug("I NEED just THE MODULE: %s", str(file_name))
                return set([str(file_name)])
            if import_modules:
                logger.debug("No filename parsed, use the module: %s",
                             obj.__module__)
                return set([obj.__module__])
            logger.debug("No filename parsed, use the FQDN: %s",
                         obj.__module__)
            return set([f"{obj.__module__}.{obj.__name__}"])
        if import_modules:
            logger.debug("%s %s missing __code__ < I need this module!", loc, obj)
        else:
            logger.debug("%s type_str=%s < I need this FQDN!", loc, type_str)

    # pylint: disable-next=too-many-nested-blocks
    elif "." in type_str:
        if import_modules:
            logger.debug("%s type_str=%s for %s; adding %s (recursion_depth=%d)",
                         loc, type_str, decoratee, parsed_type, recursion_depth)
            all_types.add(parsed_type)
            # Add all non-builtin sub-types of object
            # If obj is a composite object (e.g. a class) comprised of any
            # non-built in objects (e.g. other classes), I need to add
            # all subtypes recursively.
            if hasattr(obj, "__dict__"):
                for k,v in obj.__dict__.items():
                    if isinstance(obj.__dict__[k], dict):
                        #logger.debug("Adding %s:%s from composite dict",
                        #             k, type(obj.__dict__[k]))
                        for v2 in obj.__dict__[k].values():
                            #all_types.add(type(k))
                            all_types |= get_all_types("6",
                                                       v2,
                                                       import_modules,
                                                       recursion_depth+1,
                                                       decoratee)

                    if isinstance(obj.__dict__[k], (set, list, tuple)):
                        #logger.debug("Adding %s:%s from composite",
                        #             k, type(obj.__dict__[k]))
                        for v2 in obj.__dict__[k]:
                            #all_types.add(type(k))
                            all_types |= get_all_types("6",
                                                       v2,
                                                       import_modules,
                                                       recursion_depth+1,
                                                       decoratee)

                return all_types
            logger.debug("WHAT TO DO? %s type_str=%s for %s; adding %s",
                         loc, type_str, decoratee, parsed_type)
        else:
            logger.debug("%s type_str=%s for %s (recursion_depth=%d)!",
                         loc, type_str, decoratee, recursion_depth)
            if parsed_type_match:
                if parsed_type and parsed_type.startswith("__main__"):
                    ext_module_file = inspect.getfile(obj.__class__)
                    logger.info(ext_module_file)
                    file_name = get_filename(ext_module_file)
                    if file_name:
                        ext_module_file = file_name
                        logger.info(ext_module_file)
                        fqn = re.sub("__main__", ext_module_file, parsed_type)
                        logger.info(fqn)
                        return set([fqn])
                logger.info(parsed_type)
                all_types.add(parsed_type)
                return all_types

    if isinstance(obj, dict):
        for v in obj.values():
            all_types |= get_all_types("6", v, import_modules, recursion_depth+1, decoratee)

    elif inspect.isclass(obj):
        logger.critical("%s is a class", obj)
        return all_types

    # Now handle all other iterables aside from dictionaries
    # Non-iterables will throw a TypeError but that's perfectly ok
    elif not isinstance(obj, str):
        try:
            for obj_i in obj:
                all_types |= get_all_types("7", obj_i, import_modules, recursion_depth+1, decoratee)
        except TypeError as e:
            logger.critical(e)

    result = set()
    for this_type in all_types:
        parsed_type_match = re.match("<class '([^']+)'>", str(this_type))
        if parsed_type_match:
            expected_type = parsed_type_match.groups()[0]
            logger.debug("Adding %s", expected_type)
            result.add(expected_type)
        else:
            result.add(this_type)

    if result:
        logger.debug("result=%s", result)
    return result


def generate_all_tests_and_metadata_helper( local_all_metadata:defaultdict[str, typing.Any],
                                            function_names:list[str],
                                            outdir:Path,
                                            tests_dir:Path,
                                            ext:Path=Path(".json"))->defaultdict[str, typing.Any]:
    """
    This function generates units tests for decorated functions and methods.

    Because I also decorate functions within this very file
    (i.e. the functions and methods that implement the automatic unit
    test generation), it's necessary to call this function twice to
    ensure that unit tests are created for all functions and
    methods defined within this very file.

    I do claim this is self-testing code after all!
    """

    #pp.pprint(local_all_metadata)
    for function_name in function_names:
        logger.debug("function_name=%s", function_name)
        function_metadata:FunctionMetaData = copy.deepcopy(local_all_metadata[function_name])
        test_suite = function_metadata.coverage_io
        # The json file is optional and unused but makes for
        # friendly reading of the inputs to the unit test if
        # the actual .py unit test file is hard to read
        # due to formatting.
        this_function_name = re.sub(".__init__", ".constructor", function_name)
        filename = outdir.joinpath(f"{this_function_name}{ext}")
        with open(filename, "w", encoding="utf-8") as test_io_file:
            logger.info("Dumping test metadata to %s...", str(filename))
            json.dump(function_metadata,
                      test_io_file,
                      cls=FunctionMetaDataEncoder,
                      indent=3
                      )
        if not test_suite:
            logger.debug("No test record for %s", function_name)
            continue
        auto_generate_tests(local_all_metadata[function_name],
                            test_suite,
                            function_name,
                            function_metadata.source_file,
                            tests_dir)
        local_all_metadata.pop(function_name)
    return local_all_metadata

@unit_test_generator_decorator(sample_count=0)
def generate_all_tests_and_metadata(outdir:Path,
                                    tests_dir:Path,
                                    suffix:Path=Path(".json")):
    """
    Called once the ad-hoc/integration/regression tests
    are completed, this function writes all the results
    of using the unit_test_generator_decorator() decorator
    to files, one file per decorated function.

    The first 'Before' call to
    generate_all_tests_and_metadata_helper()
    created new entries for the 'all_metadata' dictionary because it
    called functions/methods within this very file that are also
    decorated with @unit_test_generator_decorator!
    Talk about meta-programming and meta-testing. =D

    Call generate_all_tests_and_metadata_helper twice
    to generate unit tests for
    to test the functions and methods defined in this
    file and called by generate_all_tests_and_metadata_helper()
    """
    for phase in ["Before", "After"]:
        logger.debug("phase=%s", phase)
        #pp.pprint(all_metadata)

        logger.debug("%s: %s", phase, all_metadata.keys())

        function_names = copy.deepcopy(list(all_metadata.keys()))
        local_all_metadata = all_metadata
        local_all_metadata = generate_all_tests_and_metadata_helper(local_all_metadata,
                                                                    function_names,
                                                                    outdir,
                                                                    tests_dir,
                                                                    suffix)

@unit_test_generator_decorator(sample_count=1)
def update_global(obj,
                  this_global:str,
                  phase:str,
                  this_coverage_info:CoverageInfo)->CoverageInfo:
    """
    Update and return state dictionary with new global.
    """
    if repr(obj).startswith("<"):
        logger.critical("Skipping %s", obj)
        return this_coverage_info
    if isinstance(obj, set):
        this_entry = sorted_set_repr(obj)
        updated_entry = copy.deepcopy(this_entry)
    else:
        updated_entry = copy.deepcopy(obj)
    # The block below is for a separate project
    #if this_global == "g_function_params_write_locs":
        #logger.critical(f"{this_global=}\n{obj=}")

    #print(f"{this_global}={this_entry}")

    #updated_entry = this_entry

    if phase == "Before":
        this_coverage_info.globals_before[this_global] = updated_entry
    elif phase == "After":
        this_coverage_info.globals_after[this_global] = updated_entry
    return this_coverage_info


@unit_test_generator_decorator(sample_count=1)
def normalize_arg(arg:typing.Any)->typing.Any:
    """
    Convert arg to "canonical" form; i.e. convert it to a string format such
    that by writing it to a file it becomes proper Python code.
    """
    if isinstance(arg, str):
        arg = re.sub("<class '([^']+)'>", "\\1", arg)
    if arg == "false":
        arg = "False"
    elif arg == "true":
        arg = "True"
    # Trim quotes so types are used rather than just the string representation
    if isinstance(arg, str) and ((arg[0] == '"' and arg[-1] == '"') or \
                                 (arg[0] == "'" and arg[-1] == "'")):
        arg = arg[1:-1]
    return arg

def normalize_string(arg:str)->str:
    """
    Return canonical representation of string
    """
    if (arg[0] == "'" and arg[-1] == "'") or (arg[0] == '"' and arg[-1] == '"'):
        arg = re.sub(r'(?<!^)(?<!\\)"(?!$)', r'\\"', arg)
    return arg

@unit_test_generator_decorator(sample_count=1)
def coverage_str_helper(this_list:list, non_code_lines:set)->list[str]:
    """
    Given a 'this_list', containing numbers covered or uncovered,
    and a set of non_code_lines (comments or whitespace),
    Generate a list that compactly represents the (un) covered lines.
    e.g.
    this_list=[1,2,3,4,7,8,9], non_code_lines={5,6} -> ["1-4", "7-9"]
    """
    results_list = []
    if not this_list:
        results_list.append("N/A")
    pending_update = False
    results_list = []
    low_number = this_list[0]
    high_number = low_number
    for line_number in this_list[1:]:
        if line_number == high_number + 1:
            high_number = line_number
            pending_update = True
            continue
        if line_number in non_code_lines:
            continue
        if low_number != high_number:
            results_list.append(f"{low_number}-{high_number}")
            pending_update = False
        else:
            results_list.append(str(low_number))
            pending_update = False
        low_number = line_number
        high_number = line_number
    if pending_update:
        if low_number != high_number:
            results_list.append(f"{low_number}-{high_number}")
            pending_update = False
        else:
            results_list.append(str(low_number))
            pending_update = False

    if not results_list:
        if low_number == high_number:
            results_list.append(low_number)
        else:
            logger.critical("Invalid coverage! %s", this_list)

    return results_list

@unit_test_generator_decorator(sample_count=0)
def gen_coverage_list(  function_metadata:FunctionMetaData,
                        coverage_list:list,
                        function_name:str,
                        tab:str=" "*3):
    """
    Given a state[hash_key] and function name create a comment string
    to show lines covered, percent covered, and lines not covered
    """
    first_source_line_num = function_metadata.lines[0]
    last_source_line_num = function_metadata.lines[-1]
    range_source_line_nums = set(range( first_source_line_num,
                                        last_source_line_num+1))
    coverage_set = set(coverage_list)
    coverage_list = sorted(list(range_source_line_nums & coverage_set))
    if not coverage_list:
        logger.warning("Fix the bug here; no coverage for %s", function_name)
        return []
    non_code_lines = function_metadata.return_non_code_lines()

    logger.debug("coverage_list=%s", coverage_list)
    logger.debug("range_source_line_nums=%s", range_source_line_nums)
    logger.debug("function_name=%s", function_name)
    if logger.level >= logging.DEBUG:
        msg = pp.pformat(function_metadata.lines)
        logger.debug("lines=%s", msg)

    # Subtract one for the function
    percent_covered = 100*len(coverage_list)/(len(function_metadata.lines))
    #percent_covered = 100*percent_covered
    coverage_str_list = []
    start_list = []
    start_list.append(f"{tab}# Coverage: {percent_covered:.2f}% of function lines ")
    start_list.append(f"[{first_source_line_num}-{last_source_line_num}]\n")
    start_list.append(f"{tab}# Covered Lines: ")
    start = ''.join(start_list)
    uncovered_str_list = []
    start2 = f"{tab}# Lines not covered: "
    # Create the uncovered list now for use laster in this function
    uncovered = sorted(list(range_source_line_nums - set(coverage_list)))

    # Add dummy (-1) to the end of the un/covered lists,
    # otherwise the real last element won't be included
    coverage_list.append(-1)
    if uncovered:
        uncovered.append(-1)

    coverage_str_list = coverage_str_helper(coverage_list, non_code_lines)
    if uncovered:
        uncovered_str_list = coverage_str_helper(uncovered, non_code_lines)

    end = f"{tab}# Note: Any lines not mentioned are comments or whitespace\n"
    logger.debug(coverage_str_list)
    result = [f"\n{start}{';'.join(coverage_str_list)}"]
    result.append(f"\n{start2}{';'.join(uncovered_str_list)}\n{end}")
    return result

# pylint: disable=too-many-locals,too-many-branches
@unit_test_generator_decorator(sample_count=1)
def meta_program_function_call( this_state:CoverageInfo,
                                tab:str,
                                package,
                                function_metadata:FunctionMetaData)->list[str]:
    """
    Given the provided arguments,
    return a list of valid Python code that executes the decorated
    function and asserts that the result is as expected.
    """
    expected_type = this_state.expected_type
    function_name = function_metadata.name
    parameter_names = function_metadata.parameter_names
    try:
        parameter_names.remove("self")
    except ValueError:
        pass
    class_var_name = ""
    is_method = False
    list_of_lines = []
    #singletons = [None, True, False]
    indent = tab*2
    # Handle the case that decoratee is a
    # class method by constructing the class
    if this_state.constructor:
        #function_name=function_name.split('.')[1]
        class_var_name = "test_class_instance"
        is_method = True # Marginally faster than this string compare?
        #line = f"{indent}{class_var_name} = {this_state.constructor}\n"
        #list_of_lines.append(line)

    kwargs_str = ''
    if this_state.kwargs:
        # Creating "line" variable to condense line width
        line = f"{indent}kwargs = {this_state.kwargs}\n"
        list_of_lines.append(line)
        kwargs_str = ", kwargs=kwargs)"

    call = ""
    if is_method:
        prefix = f"{class_var_name}.{function_name.split('.')[1]}"
        if len(this_state.args) != 1:
            call = f"{prefix}({','.join(parameter_names)}{kwargs_str})\n"
        elif len(this_state.args):
            #arg = normalize_string(this_state.args[0])
            #list_of_lines.append(f"{indent}arg = {arg}\n")
            call = f"{prefix}({parameter_names[0]}{kwargs_str})\n"

    else:
        prefix = f"{package}.{function_name}"
        if len(this_state.args) != 1:
            call = f"{prefix}({','.join(parameter_names)}{kwargs_str})\n"
        elif len(this_state.args):
            call = f"{prefix}({parameter_names[0]}{kwargs_str})\n"

    # If any exceptions were caught when testing this function, add this code:
    if bool(function_metadata.exceptions_raised):
        # Source: https://docs.pytest.org/en/6.2.x/assert.html#assertraises
        line = f"{indent}if exception_type != 'N/A':\n"
        indent += tab
        list_of_lines.append(line)
        line = f'{indent}with pytest.raises(exception_type, match=re.escape(exception_message)):\n'
        indent += tab
        list_of_lines.append(line)
        line = f'{indent}{call}'
        list_of_lines.append(line)
        indent = indent[:-len(tab)]

        list_of_lines.append(f"{tab*2}else:\n")
        #indent = indent[:-len(tab)]


    normal_call = f"{indent}result = {call}"
    if function_name.endswith(".__init__"):
        #function_name = re.sub(".__init__", "", function_name)
        normal_call = re.sub(".__init__", "", normal_call)
    list_of_lines.append(normal_call)
    if not this_state.expected_result:
        line = f"{indent}assert not result\n"
    else:
        result_str = ""
        logger.debug("function_name=%s", function_name)
        if expected_type == "str":
            logger.debug("String: %s", this_state)
            result_str = this_state.expected_result
            result_str = result_str.replace("'", "\\'")
            result_str = result_str.replace('"', '\\"')
            result_str = f"\'{result_str}\'"
            logger.debug(result_str)
        else:
            result_str = this_state.expected_result
            result_str = normalize_arg(this_state.expected_result)
            logger.debug(result_str)
        assert not result_str.startswith("'\n"), "Bad juju"
        if function_name.endswith(".__init__"):
            class_fqn = re.sub(".__init__.*$", "", call)
            line = f"{indent}assert isinstance(result, {class_fqn})\n"
            list_of_lines.append(line)
        #elif result_str in singletons:
            #line = f"{tab}assert x is {result_str}\n"
    if expected_type and expected_type != "NoneType":
        list_of_lines.append(f"{indent}assert isinstance(result, expected_type)\n")
    if "__init__" not in function_name:
        #list_of_lines.append(f"{indent}if result in {repr(singletons)}:\n")
        #indent += tab
        #list_of_lines.append(f"{indent}assert x is result\n")
        #indent = indent[:-len(tab)]
        #list_of_lines.append(f"{indent}else:\n")
        #indent += tab
        line = f"{indent}assert result == expected_result or result == eval(expected_result)\n"
        list_of_lines.append(line)
    else:
        for name in parameter_names:
            list_of_lines.append(f"{indent}assert result.{name} == {name}\n")
    return list_of_lines


@unit_test_generator_decorator(sample_count=0)
# pylint: disable-next=too-many-statements,too-many-locals,too-many-branches,too-many-arguments
def auto_generate_tests(function_metadata:FunctionMetaData,
                        state:dict[str, CoverageInfo],
                        function_name:str,
                        source_file:Path,
                        tests_dir:Path,
                        indent_size:int=2)->str:
    """
    This is the function that can automatically create a unit
    test file for each decorated function.
    The contents of the unit test file(s) are created by appending
    to lists of strings, these lists of strings are evenutally
    written to a file, one per decorated function.
    """

    imports = ["import re\n","import pytest\n"]

    was_executed = False
    globals_before_are_constant = True
    constant_globals_before: dict[str, typing.Any] = {}
    constant_globals_before_key = set()

    # Only functions/methods that accessed global
    # variables will need to be patched
    # The variable below will help us keep track of this.
    needs_monkeypatch = False

    # NOTE: Add to the import list any specific modules for
    # which repr doesn't work, e.g.
    # imports.append(import pandas as pd\n")

    try:
        last_key, last_element = state.popitem()
        if last_element.globals_before:
            for gbk, gbv in last_element.globals_before.items():
                if all(v.globals_before[gbk] == gbv for v in state.values()):
                    logger.info("Constant pre-global '%s' for %s", gbk, function_name)
                    constant_globals_before[gbk] = gbv
                    constant_globals_before_key.add(gbk)
                else:
                    logger.info("Varying pre-global '%s' for %s", gbk, function_name)
                    globals_before_are_constant = False
        state[last_key] = last_element
    except KeyError:
        globals_before_are_constant = False

    if globals_before_are_constant:
        logger.info("All globals before call are constant.")

    tab = " "*indent_size
    raise_ex_msg = f"{tab}raise Exception('{function_name} was never executed')"

    header = []
    for k, v in constant_globals_before.items():
        header.append(f"{k.upper()} = {v}\n")


    pct = function_metadata.coverage_percentage
    #assert pct <= 100, "Bad math"
    line = f"{tab}# In sum, these tests covered {pct}% of {function_name}'s lines\n"
    header.append(line)
    if pct < 100:
        uncovered_str = function_metadata.get_all_uncovered_line_str()
        lines = [
                    f"{tab}# Line(s) not covered by ANY of the tests below:\n",
                    f"{tab}# {uncovered_str}\n"
                ]
        header += lines

    # pylint: disable-next=line-too-long
    test_str_list_def_dict:typing.DefaultDict[int, List[str]] = defaultdict(int) # type: ignore [arg-type]

    package = Path(source_file).stem
    initial_import_list = get_module_import_string(source_file).split(".")
    initial_import_prefix = ".".join(initial_import_list[:-1])
    initial_import_suffix = initial_import_list[-1]
    if initial_import_prefix:
        initial_import = f"from {initial_import_prefix} import {initial_import_suffix}\n"
    elif initial_import_suffix:
        initial_import = f"import {initial_import_suffix}\n"
    else:
        initial_import = ""

    book_end = f'{tab*2}\"\"\"\n'
    docstring = f'{book_end}{tab*2}'
    docstring += f"Programmatically generated test function for {function_name}()"
    docstring += f'\n{book_end}'

    is_method = function_metadata.is_method
    logger.debug("%s is method: %s", function_name, is_method)
    any_exception = False
    any_gb = False
    any_ga = False
    any_kwargs = False
    parameterization_list = ["@pytest.mark.parametrize(\n"]
    parameterization_list.append("\"")
    if is_method and "__init__" not in function_name:
        parameterization_list[1] += "test_class_instance, "
    parameterization_list[1] += f"{', '.join(function_metadata.parameter_names)}"
    if any(v.kwargs for v in state.values()):
        parameterization_list[1] += ", kwargs"
        any_kwargs = True
    if any(v.exception_type for v in state.values()):
        parameterization_list[1] += ", exception_type, exception_message"
        any_exception = True
    parameterization_list[1] += ", expected_result, expected_type"
    if any(v.globals_before for v in state.values()):
        parameterization_list[1] += ", globals_before"
        any_gb = True
    if any(v.globals_after for v in state.values()):
        parameterization_list[1] += ", globals_after"
        any_ga = True
    parameterization_list[1] += '\",\n['

    if "self" in parameterization_list[1]:
        # Chop off leading "self," parameter
        parameterization_list[1] = re.sub("self, ", '', parameterization_list[1])
    clean_fn: str = function_name.lower().replace('.','_')
    test_str_list = [   f"def test_{clean_fn}({parameterization_list[1][1:-4]}):\n",
                        docstring,
                        "# Monkeypatch here"
                    ]
    for hash_key in sorted(state):
        globals_before = {k:normalize_arg(v) for k, v in state[hash_key].globals_before.items()}
        globals_after = {k:normalize_arg(v) for k, v in state[hash_key].globals_after.items()}
        new_params = []
        if is_method and "__init__" not in function_name:
            new_params.append(state[hash_key].constructor)
        new_params.append(','.join(state[hash_key].args))
        if any_kwargs:
            if state[hash_key].kwargs:
                new_params.append(','.join(state[hash_key].kwargs))
            else:
                new_params.append('"N/A"')
        if any_exception:
            if state[hash_key].exception_type:
                new_params.append(state[hash_key].exception_type.split("'")[1])
            else:
                new_params.append('"N/A"')
            if state[hash_key].exception_message:
                new_params.append(repr(state[hash_key].exception_message))
            else:
                new_params.append('"N/A"')
        new_params.append(repr(state[hash_key].expected_result))
        if state[hash_key].expected_type == "NoneType":
            new_params.append('"N/A"')
        else:
            new_params.append(state[hash_key].expected_type.split('.')[-1])
        if any_gb:
            new_params.append('{}' if not globals_before else repr(globals_before))
        if any_ga:
            new_params.append('{}' if not globals_after else repr(globals_after))
        parameterization_list.append('('+",".join(new_params)+'),\n')

    #test_str_list += parameterization_list
    for hash_key_index, hash_key in enumerate(sorted(state)):
        this_parameterization =""# f"({','.join(state[hash_key].args)}"
        monkey_patches = []
        if state[hash_key].globals_before:
            monkey_patches.append(f"{tab*2}for k, v in globals_before.items():\n")
        grv_str_list: list[str] = []
        for k in sorted(state[hash_key].globals_before):
            needs_monkeypatch = True
            #test_str_list.append(f"{tab}monkeypatch = MonkeyPatch()\n")
            v = state[hash_key].globals_before[k]
            v = normalize_arg(v)


            if k in constant_globals_before_key:
                grv_str_list.append(k.upper())
                line = f'{tab*3}monkeypatch.setattr({package}, \"{k}\", {k.upper()})\n'
            else:
                grv_str_list.append(k)
                line = f'{tab*3}monkeypatch.setattr({package}, k, v)\n'
            monkey_patches.append(line)

        if monkey_patches:
            test_str_list += monkey_patches
        #monkey_patches = []

        gwv_str_list: list[str]  = []
        for k in sorted(state[hash_key].globals_after):
            v = state[hash_key].globals_after[k]
            #this_parameterization += f"{v}, "
            gwv_str_list.append(k)
            #paramterization_list[1] += f"{k},"
            v = state[hash_key].globals_after[k]
            v = normalize_arg(v)
        test_str_list += this_parameterization

        test_str_list += meta_program_function_call(state[hash_key],
                                                    tab,
                                                    package,
                                                    function_metadata)
        dict_get = ".__dict__.get"

        if sorted(state[hash_key].globals_after):
            gvwt = "global_var_written_to"
            line = f"{tab*2}for {gvwt} in {repr(sorted(state[hash_key].globals_after.keys()))}:\n"
            test_str_list.append(line)
            test_str_list.append(f"{tab*3}if {gvwt} in ['None', '[]', '{{}}']:\n")
            line = f'{tab*4}assert not {package}{dict_get}({gvwt})\n'
            line = re.sub("<class '([^']+)'>", "\\1", line)
            test_str_list.append(line)
            test_str_list.append(f"{tab*3}else:\n")
            line = f'{tab*4}assert {package}{dict_get}({gvwt}) == globals_after[{gvwt}]\n'
            line = re.sub("<class '([^']+)'>", "\\1", line)
            test_str_list.append(line)
            needs_monkeypatch = True

        #test_str_list += monkey_patches
        # Delete all references to "__main__", it's needless
        #print(test_str_list)
        test_str_list = [re.sub("__main__.", "", x) for x in test_str_list]
        if not test_str_list:
            # If this function was never executed, its coverage is 0%
            # Raise an exception to alert the user
            # Note that we don't need any imports at all
            test_str_list.append(raise_ex_msg)

        if test_str_list:
            if needs_monkeypatch:
                test_str_list[2] = f"{tab*2}monkeypatch = MonkeyPatch()\n"
            else:
                test_str_list.pop(2)

            test_str_list_def_dict[hash_key_index] = test_str_list
            was_executed = True
        break
    # End of loop over all samples

    if was_executed:
        imports.append(initial_import)

    # Only functions/methods that access
    # global variables will need to be patched
    if needs_monkeypatch:
        imports.append("from _pytest.monkeypatch import MonkeyPatch\n")

    custom_imports = []

    for this_type in function_metadata.types_in_use:
        continue_flag = False
        for other_type in function_metadata.types_in_use:
            if this_type == other_type:
                continue
            if other_type.endswith(this_type):
                continue_flag = True
                break
        if continue_flag:
            continue
        splits = this_type.split(".")
        prefix = '.'.join(splits[:-1])
        module = splits[-1]
        if not module:
            logger.error("NO MODULE")
            continue
        if prefix == "__main__":
            if package:
                custom_imports.append(f"from {package} import {module}\n")
        elif prefix:
            custom_imports.append(f"from {prefix} import {module}\n")
        elif module:
            custom_imports.append(f"import {module}\n")

    if custom_imports:
        imports.append("\n")
        imports.append(f"# Now import modules specific to {function_name}:\n")
    imports += custom_imports

    logger.debug("function_name=%s", function_name)
    result_file_str = f"test_{function_name.lower()}".replace('.','_') + ".py"
    result_file_str = re.sub("__init__", "constructor", result_file_str)
    result_file = tests_dir.joinpath(result_file_str)

    if "pytest" in sys.modules:
        # Return hash of resulting string here,
        # this is used when self-testing auto_generate_tests with
        # unit_test_generator_decorator
        h = hashlib.new('sha256')
        h.update(str(sorted(test_str_list_def_dict.items())).encode())
        return h.digest().hex()

    parameterization_list[-1] += "])\n"
    docstring = f'\"\"\"\nProgrammatically generated test function for {function_name}()\n\"\"\"'
    with open(result_file, "w", encoding="utf-8") as st:
        st.write(docstring+"\n")
        for item in [imports, header, parameterization_list]:
            if item:
                st.writelines(item)
        for item in test_str_list_def_dict.values():
            st.writelines(item)

    logger.info("Wrote to %s", result_file)

    # Format the generated Python file with black for easier reading

    try:
        subprocess.run( f"black {result_file}".split(),
                        check=True,
                        capture_output=True
                        )
    except CalledProcessError as e:
        logger.error("Got Error running black formatter on %s:", result_file)
        logger.error("%s", pp.pformat(e)+"\n")
        logger.error("%s", e.stderr.decode()+"\n")
        if e.stdout:
            logger.error(e.stdout.decode())

    logger.info("Re-formatted %s with black formatter", result_file)

    try:
        subprocess.run( f"ruff {result_file} --fix".split(),
                        check=True,
                        capture_output=True
                        )
    except CalledProcessError as e:
        logger.error("Got Error running ruff linter on %s:", result_file)
        logger.error("%s", pp.pformat(e)+"\n")
        logger.error("%s", e.stderr.decode()+"\n")
        if e.stdout:
            logger.error(e.stdout.decode())

    logger.info("Linted %s with ruff", result_file)

    # Return hash of resulting string here
    h = hashlib.new('sha256')
    h.update(str(sorted(test_str_list_def_dict.items())).encode())
    return h.digest().hex()
