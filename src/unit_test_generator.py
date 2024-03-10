import re
import os
import sys
import json
import copy
import time
import types
import hashlib
import inspect
import traceback
import pprint
import logging
import coverage
import subprocess
import pandas as pd

from dis import dis
from io import StringIO
from functools import wraps
# NOTE: WindowsPath is in fact required if running on Windows!
from pathlib import Path, WindowsPath
from json import JSONEncoder
from collections import defaultdict
from subprocess import CalledProcessError
from types import MappingProxyType
from collections.abc import Callable
import typing

pp = pprint.PrettyPrinter(indent=3)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set this value to disable the
# unit_test_generator_decorator once coverage hits
# this value as a percent, e.g. 80 = 80% coverage
coverage_cutoff = 100
recursion_depth_per_decoratee = defaultdict(int)

active = False

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

def unit_test_generator_decorator(active:bool):
    def actual_decorator(func:Callable):
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

        When the coverage percent (as measured by $lines_executed/$lines_in_file)
        meets or exceeds coverage_cutoff, this wrapper will
        deactivate and simply return the results of the function, ceasing to
        track any further coverage and removing the overhead involved in such
        monitoring.

        When main() completes, main() writes out the coverage results to one file
        per decorated function.
        """
        @wraps(func)
        def unit_test_generator_decorator_inner(*args, **kwargs):
            if not active:
                return func(*args, **kwargs)
            global recursion_depth_per_decoratee
            if "pytest" in sys.modules:
                logger.debug("pytest is loaded; don't decorate when under a test")
                result = func(*args, **kwargs)
                return result

            function_calls = None
            function_calls = defaultdict(int)

            for f in inspect.stack()[::-1]:
                F = inspect.getframeinfo(f[0])
                function_calls[F.function] += 1
            if func.__name__ not in recursion_depth_per_decoratee:
                recursion_depth_per_decoratee[func.__name__] = max(function_calls.values())

            elif 1 < max(function_calls.values()) >= recursion_depth_per_decoratee[func.__name__]:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logger.critical(e)
                    raise e
            try:
                return do_the_decorator_thing(func, *args, **kwargs)
            except Exception as e:
                logger.warning("e=%s", e, exc_info=True)
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

pd.DataFrame.__repr__ = _pandas_df_repr

def get_module_import_string(my_path:Path):
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
            logger.debug("os.path.relpath(file, my_path, )=%s", os.path.relpath(file, my_path, ))
            this_type = f"{os.path.relpath(file, my_path)}"
    if keep_file:
        my_path_str = str(my_path)[len(str(keep_file)):]
        my_path_str = re.sub(r"^[\\/]", "", my_path_str)
        this_type = re.sub(".py$", "", my_path_str)
        if not this_type:
            return
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
        file = Path(file)
        if my_path.is_relative_to(file):
            keep_file = file
            this_type = f"{os.path.relpath(file, my_path)}"
    if keep_file:
        my_path_str = str(my_path)[len(str(keep_file)):]
        my_path_str = re.sub(r"^[\\/]", "", my_path_str)
        this_type = re.sub(".py$", "", my_path_str) + "." + arg.__class__.__qualname__
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

@unit_test_generator_decorator(active)
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

# TODO Import any modules here for whom 'repr' doesn't work
from pandas import DataFrame

pp = pprint.PrettyPrinter(indent=3)

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

# Set this value to disable the
# unit_test_generator_decorator once coverage hits
# this value as a percent, e.g. 80 = 80% coverage
coverage_cutoff = 60

def do_the_decorator_thing(func, *args, **kwargs):
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

    When the coverage percent (as measured by $lines_executed/$lines_in_file)
    meets or exceeds coverage_cutoff, this wrapper will
    deactivate and simply return the results of the function, ceasing to
    track any further coverage and removing the overhead involved in such
    monitoring.

    When main() completes, main() writes out the coverage results to one file
    per decorated function.
    """
    global all_metadata, timestamps
    this_metadata = None
    caught_exception = None
    if 'kwargs' in kwargs:
        kwargs = kwargs['kwargs']

    func_name = str(func).split()[1]
    #logger.critical(f"Decorating {func_name}".center(80, '-'))

    '''
    if func_name in all_metadata and\
        all_metadata[func_name].coverage_percentage >= coverage_cutoff:
        logger.debug(f"Hit >={coverage_cutoff=} in {func_name}; skip it.")
        x = func(*args, **kwargs)
        #logger.critical(f"Undecorating {func_name}".center(80, '-'))
        return x
    '''

    if "pytest" in sys.modules:
        logger.debug("pytest is loaded; don't decorate when under a test")
        x = func(*args, **kwargs)
        #logger.critical(f"Undecorating {func_name}".center(80, '-'))
        return x

    source_file = Path(func.__code__.co_filename).absolute()

    # If this is the first time this func has been called, disassemble
    # it to get the lines and global variables
    if func_name and func_name not in all_metadata:
        # Using single var names ('x', 'y') to keep lines short
        (x, y, z) = return_function_line_numbers_and_accessed_globals(func)

        this_metadata = FunctionMetaData(   name=func_name,
                                            lines=x,
                                            is_method='.' in func_name,
                                            global_vars_read_from=y,
                                            global_vars_written_to=z,
                                            source_file=source_file
                                        )
        logger.debug("%s has source line #s: %d-%d", func_name, min(x), max(x))

    elif func_name in all_metadata:
        this_metadata = all_metadata.pop(func_name)

    state = {   "Before":{'globals':dict()},
                "After":{'globals':dict()},
            }

    #args_copy = [convert_to_serializable(x) for x in args]
    args_copy = []
    class_type = None
    if this_metadata.is_method and not func_name.endswith("__init__"):
        logger.critical(f"{func_name=}")
        state['Constructor'] = args[0].repr()

        this_type = get_class_import_string(args[0])
        class_type = copy.deepcopy(this_type)

    new_types_in_use = set()

    for arg_i, arg in enumerate(args):
        # Do not include the first arg of a method (it's "self")
        # in the argument list
        if this_metadata.is_method and arg_i == 0:
            continue
        if callable(arg) and  inspect.isfunction(arg) and "." in arg.__qualname__ and arg.__qualname__[0].isupper():
            newest_import = f"{arg.__module__}.{arg.__qualname__}".split('.')
            newest_import = '.'.join(newest_import[:-1])
            args_copy.append(arg.__qualname__)
            try:
                # Reset the class type, as this newes_import will be used
                # instead
                class_type = None
                if arg.__module__ == "__main__":
                    file_name = re.search(r"([\w]+).py", str(arg.__code__))
                    if file_name:
                        file_name = file_name.groups()[0]
                        newest_import = re.sub("__main__", file_name, newest_import)
                    else:
                        logger.critical("NO FILENAME FOUND!: %s", re.escape(str(arg.__code__)))
                new_types_in_use.add(newest_import)


            except Exception as e:
                print(traceback.format_exc())
                logger.critical(e)
                sys.exit(2)
            continue

        new_types_in_use |= get_all_types("1", arg, False)
        if hasattr(arg, "__dict__"):
            for v in arg.__dict__.values():
                new_types_in_use |= get_all_types("1.1", v, False)
        if callable(arg):
            if arg.__module__ == "__main__":
                file_name = re.search(r"([\w]+).py", str(arg.__code__))
                if file_name:
                    file_name = file_name.groups()[0]
                    logger.debug("%s.%s",file_name, arg.__name__)
                    args_copy.append(f"{file_name}.{arg.__name__}")
                else:
                    logger.critical("NO FILENAME FOUND!: %s", re.escape(str(arg.__code__)))
            else:
                args_copy.append(arg.__qualname__)

            #sys.exit(1)
        elif not isinstance(arg, str):
            type_str = str(type(arg))
            #logger.critical(arg)
            #logger.debug(f"{type_str} {type(arg).__module__}")

            # Reference for line:
            # 'type(arg).__module__ != "__builtin__":'
            # https://stackoverflow.com/questions/46876484/
            # Answer by user moar10
            if bool(re.match(r"<class[^\.]+\.", type_str)) and\
                type(arg).__module__ != "__builtin__":
                try:
                    class_repr = arg.repr()

                except AttributeError as e:
                    class_repr = arg.__repr__()
                #logger.debug(f"Got class!: {class_repr}")
                try:
                    logger.info(class_repr)
                    eval(class_repr)
                    args_copy.append(class_repr)
                except SyntaxError as e:
                    # skip on error
                    logger.debug("Got %s %s decorating %s repr'ing arg=%s:\ne=%s", type(e), class_repr, func_name, arg, e)
                    x = func(*args, **kwargs)
                    all_metadata[func_name] = this_metadata
                    return x
                except NameError as e:
                    # What's going on here?
                    # This argument (arg) is a class, but that class hasn't
                    # been imported, so calling "eval" on
                    # it yielded a NameError.  No problem, assume that we
                    # can import it later; now we simply record it as one of
                    # the arguments to this decoratee by adding it to args_copy.
                    logger.debug(e)
                    logger.debug("class_repr=%s arg=%s", class_repr, arg)

                    args_copy.append(class_repr)
            else:
                args_copy.append(repr(arg))
        else:
            args_copy.append("\""+re.sub(r"(?<!\\) \"", r'\\"',arg)+"\"")

    if class_type:
        this_metadata.types_in_use.add(class_type)
    this_metadata.types_in_use |= new_types_in_use

    state['Before']['args'] = args_copy

    phase = "Before"
    # Record the values of any global variables READ BY this function
    for this_global in this_metadata.global_vars_read_from:
        obj = func.__globals__[this_global]
        state = update_global(obj, this_global, phase, state)
        these_types = get_all_types("2", func.__globals__[this_global])
        this_metadata.types_in_use |= these_types
    # Also record globals variables WRITTEN TO by the function, as we may
    # need to know their values in order to assert the "After"
    # values are correct once the function executes.
    # (E.g. if the function appends to a previously populated list)
    for this_global in this_metadata.global_vars_written_to:
        obj = func.__globals__[this_global]
        state = update_global(obj, this_global, phase, state)
        these_types = get_all_types("3", func.__globals__[this_global])
        this_metadata.types_in_use |= these_types

    start_time = None
    end_time = None
    cov_report_ = None
    timestamp = None
    result = None
    data_file = f"coverage_{func_name}_{time.perf_counter()}"
    cov = coverage.Coverage(data_file)
    with cov.collect():
        try:
            if kwargs:
                state['Before']['kwargs'] = kwargs
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
            else:
                start_time = time.perf_counter()
                result = func(*args)

            logger.debug("No exception :)")
        except Exception as e:
            #this_metadata.exceptions[timestamp] = e
            logger.debug("Caught e=%s", e)
            caught_exception = e
            #raise caught_exception'
        finally:
            end_time = time.perf_counter()
    with Capturing() as stdout_lines:
        cov.json_report(outfile='-')
    # result will not exist if the function threw an exception
    cov_report_ = json.loads(stdout_lines[0])
    timestamp = f"{func_name}_{time.time_ns()}"#cov_report_['meta']['timestamp']
    if caught_exception:
        logger.debug("caught_exception=%s @ %s result=%s", caught_exception, timestamp, result)

    result_type = str(type(result))
    parsed_type = re.match("<class '([^']+)'>", result_type)
    if parsed_type:
        result_type = parsed_type.groups()[0]

    this_metadata.types_in_use |= get_all_types("4", result)
    assert timestamp not in timestamps
    this_metadata.result_types[timestamp] = result_type
    #timestamps.add(timestamps)

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

    if delta == 0:
        all_metadata[func_name] = this_metadata
        logger.debug("No new coverage decorating %s; skipping.", func_name)
        if caught_exception:
            raise caught_exception
        return result

    pct_improvement = delta / len(this_metadata.lines)
    pct_improvement = round(100*pct_improvement, 4)

    log_message = f"{func_name=}; {len(this_coverage)=}"
    logger.debug(log_message)
    log_message = f"({pct_covered=}%) ({delta=}) {pct_improvement=}"
    logger.debug(log_message)

    # Keeping the code below as it may better when implementing the
    # minimal set cover problem

    # Deepcopy of keys permits modification of the dictionary in the loop
    tmp_key_list = list(this_metadata.test_coverage.keys())
    key_list = copy.deepcopy(tmp_key_list)
    for key in key_list:
        prev_coverage = this_metadata.test_coverage[key]
        # Discard this test if it covered a subset of a previous test
        if this_coverage.issubset(prev_coverage):
            logger.debug("%s: discarding current test.", source_file)
            is_subset = True
            break
        # Discard all previous tests that covered a smaller subset
        # of the lines covered by this test
        if prev_coverage.issubset(this_coverage):
            logger.debug("%s removing subset coverage @ %s.", source_file, key)
            this_metadata.test_coverage.pop(key)


    # Put another way, only keep these results IF the test coverage
    # here is NOT a subset of ANY previous run
    if is_subset:
        all_metadata[func_name] = this_metadata
        if caught_exception:
            raise caught_exception
        else:
            logger.debug("%s coverage is a subset this_metadata.coverage_percentage=%s", func_name, this_metadata.coverage_percentage)
            #logger.critical(f"Undecorating {func_name}".center(80, '-'))
            return result

    logger.debug("%s coverage @%s is not a subset", func_name, timestamp)

    if caught_exception:
        logger.debug("caught_exception=%s", caught_exception)
        state['Exception'] = {}
        state['Exception']['Type'] = str(type(caught_exception))
        state['Exception']['message'] = str(caught_exception)
        this_metadata.needs_pytest = True

    if isinstance(result, DataFrame):
        state['Result'] = f"pd.DataFrame.from_dict({result.to_dict()})"
    elif isinstance(result, str):
        state['Result'] = result
    else:
        if isinstance(result, set) and result:
            state['Result'] = sorted_set_repr(result)
        else:
            state['Result'] = repr(result)

    phase = "After"
    for this_global in this_metadata.global_vars_written_to:
        obj = func.__globals__[this_global]
        state = update_global(obj, this_global, phase, state)
        these_types = get_all_types("5", func.__globals__[this_global])
        this_metadata.types_in_use |= these_types

    this_metadata.unified_test_coverage |= this_coverage
    percent_covered = this_metadata.percent_covered(2)

    logger.debug("Achieved %s% coverage %s for %s", percent_covered, func_name)
    sorted_coverage = sorted(list(this_coverage))
    logger.debug("sorted_coverage=%s", sorted_coverage)
    # TODO remove these assserts and the timestamps set
    assert set(sorted_coverage) & set(this_metadata.lines)
    state["Coverage"] = sorted_coverage
    assert not timestamp in timestamps
    timestamps.add(timestamp)
    this_metadata.coverage_percentage = percent_covered
    # TODO remove this deepcopy
    this_metadata.coverage_io[timestamp] = copy.deepcopy(state)
    this_metadata.coverage_cost[timestamp] = round(end_time - start_time, 3)
    this_metadata.test_coverage[timestamp] = this_coverage
    # TODO Remove this assert
    assert timestamp.startswith(func_name)
    #print("Cost")
    #pp.pprint(coverage_cost)

    if caught_exception:
        all_metadata[func_name] = this_metadata
        raise caught_exception
    #logger.critical(f"Undecorating {func_name}".center(80, '-'))

    all_metadata[func_name] = this_metadata
    return result

class Jsonable:
    def toJSON(self):
        return self.__dict__

class JsonableEncoder(json.JSONEncoder):
    def default(self, obj):
        logger.debug("obj=%s", obj)
        if isinstance(obj, set):
            return sorted(list(obj))
        #if isinstance(obj, type):
        #    return
        return super().default(obj)

class FunctionMetaData(Jsonable):
    """
    Class to track metadata when testing functions and methods
    """
    def __init__(   self,
                    name:str,
                    lines:list,
                    is_method:bool,
                    global_vars_read_from:set,
                    global_vars_written_to:set,
                    source_file:Path,
                    coverage_cost:dict = {},
                    coverage_io:dict = {},
                    coverage_percentage:float=0.0,
                    result_types:dict = {},
                    test_coverage:dict = {},
                    types_in_use:set = set(),
                    unified_test_coverage:set = None,
                    needs_pytest:bool = False
                ):
        # These properties are always provided
        self.name = name
        self.lines = lines
        self.is_method = is_method
        self.global_vars_read_from = global_vars_read_from
        self.global_vars_written_to = global_vars_written_to
        self.source_file = source_file

        # These properties are not provided unless this class
        # is being constructed as part of a unit test
        self.coverage_cost = {} if not coverage_cost else coverage_cost
        self.coverage_io = {} if not coverage_io else coverage_io
        self.coverage_percentage = coverage_percentage
        self.result_types = {} if not result_types else result_types
        self.test_coverage = {} if not test_coverage else test_coverage
        self.types_in_use = set() if not types_in_use else types_in_use
        # Change in style simply to keep line length below 80 characters
        if unified_test_coverage == None:
            self.unified_test_coverage = set()
        else:
            self.unified_test_coverage = unified_test_coverage
        self.needs_pytest = needs_pytest

        #self.exceptions = exceptions
        # This last property is created programmatically
        self.non_code_lines:set = self.return_non_code_lines()

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
            uncovered -= set(record["Coverage"])
        logger.debug("uncovered=%s self.non_code_lines=%s", uncovered, self.non_code_lines)
        if uncovered:
            result = coverage_str_helper(list(uncovered), self.non_code_lines)
        else:
            result = uncovered
        logger.debug("result=%s", result)
        return result


    def __str__(self):
        return f"{self.name}:\n{self.lines=}\n"

    def return_non_code_lines(self):
        first_source_line_num = self.lines[0]
        last_source_line_num = self.lines[-1]
        range_source_line_nums =   set([x for x in range(first_source_line_num,
                                                        last_source_line_num+1)
                                        ])

        non_code_lines = range_source_line_nums - set(self.lines)
        return non_code_lines

    def repr(self)->str:
        result = [f"FunctionMetaData(\"{self.name}\""]
        result.append(self.lines.__repr__())
        result.append(self.is_method.__repr__())
        result.append(self.global_vars_read_from.__repr__())
        result.append(self.global_vars_written_to.__repr__())
        result.append(self.source_file.__repr__())
        result.append(self.coverage_cost.__repr__())
        result.append(self.coverage_io.__repr__())
        result.append(self.coverage_percentage.__repr__())
        result.append(self.result_types.__repr__())
        result.append(self.test_coverage.__repr__())
        result.append(self.types_in_use.__repr__())
        result.append(self.unified_test_coverage.__repr__())
        result.append(self.needs_pytest.__repr__())
        result.append(')')
        logger.debug("result=%s", result)
        return ','.join(result)

    def __repr__(self) -> str:
        return self.repr()

    def purge_record(self, timestamp):
        # TODO add a "update_types_in_use" method
        # Convert types_in_use to a dict {timestamp:set(types_per_timestamp)}

        update_fields = [
            self.coverage_cost,
            self.coverage_io,
            self.result_types,
            self.test_coverage
        ]
        for field in update_fields:
            try:
                field.pop(timestamp)
            except KeyError as e:
                # TODO: Fix the root cause of this bug
                logger.error("Failed to pop key: %s", e)
        # TODO call self.update_types_in_use here

    def default(self):
        return _default()

    # https://stackoverflow.com/questions/3768895
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

# https://pynative.com/make-python-class-json-serializable/
class FunctionMetaDataEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return sorted(list(o))
        elif isinstance(o, MappingProxyType):
            pass
        else:
            try:
                return o.__dict__
            except AttributeError:
                pass

def _default(obj):
    if isinstance(obj, set):
        return sorted(list(obj))
    try:
        iterable = iter(obj)
    except TypeError as e:
        raise  e
    else:
        return list(iterable)
    return json.JSONEncoder.default(obj)

all_metadata = defaultdict(FunctionMetaData)
timestamps = set()

class Capturing(list):
    '''
    Use to capture STDOUT output
    '''
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
def is_global_var(this_global:str, function_globals:dict, func_name:str):
    """
    Not all global "variables" LOADed are relevant, some are just
    imported modules (e.g. os, sys, re, etc). Given a the name of a
    candidate global variable (i.e. variables LOADed or STOREd via
    LOAD_GLOBAL or STORE_GLOBAL bytecodes) and
    the 'f'unction associated with the candidate, return True if the
    candidate is not a function or module.
    """
    is_variable = False
    undesired_types = ["<class 'function'>","<class 'module'>"]
    # TODO: Find a better way to do this than a str compare!
    if this_global in function_globals and \
        str(type(function_globals[this_global])) not in undesired_types:
        #logger.debug(f"Adding {this_global}, {type(function_globals[this_global])=}")
        is_variable = True
    elif this_global in function_globals and \
    isinstance(function_globals[this_global], types.ModuleType):
        logger.debug("Got import for %s this_gloabl=%s", func_name, this_global)
    return is_variable

@unit_test_generator_decorator(active)
def return_function_line_numbers_and_accessed_globals(f: Callable):
    """
    Given a function, returns two sets:
    1. a set of the line numbers of this function's source code
    2. all global vars accessed by the provided function
    """
    try:
        f = f.__wrapped__
    except AttributeError:
        pass
    line_numbers = []

    global_vars_read_from = set()
    global_vars_written_to = set()
    dis_ = capture(dis)
    logger.debug("f=%s type(f)=%s", f, type(f))
    disassembled_function = dis_(f)
    result = []
    for line in disassembled_function.splitlines():
        #line_number = re.match(r"^([\d]+)", line)
        # There's sometimes 1 leading space
        # TODO: Determine if there's ever more than one leading space
        # preceding a line number
        line_number = re.match(r"^[ ]{0,1}([\d]+)", line)
        if line_number:
            line_numbers.append(int(line_number.groups()[0]))
        if "LOAD_GLOBAL" in line:
            this_global = line.split("(")[1].split(")")[0]
            if is_global_var(this_global, f.__globals__, f.__name__):
                global_vars_read_from.add(this_global)
        elif "STORE_GLOBAL" in line:
            this_global = line.split("(")[1].split(")")[0]
            if is_global_var(this_global, f.__globals__, f.__name__):
                global_vars_written_to.add(this_global)
    result = [
                line_numbers,
                global_vars_read_from,
                global_vars_written_to
            ]
    return result

@unit_test_generator_decorator(active)
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
        for k,v in obj.items():
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

def get_all_types(loc: str, obj, import_modules:bool=True)->set:
    """
    Return the set of all types contained in this object,
    It might be a list of sets so return {"list", "set"}
    """
    all_types = set()
    type_str = str(type(obj))
    type_list =  ['str', 'int', 'list', 'set', 'dictionry', 'dict']
    if not any(x in type_str for x in type_list):
        logger.debug("%s type_str=%s", loc, type_str)
    if callable(obj):
        if hasattr(obj, "__code__"):
            logger.debug("%s %s.%s as callable", loc, obj.__module__, obj.__name__)
            # TODO: This is
            # 1. Redundant, the line below is duplicated elsewhere
            # 2. Perhaps not complete, I may need the (partial)
            #    path to the python file, not such the file itself
            file_name = re.search(r"([\w]+).py", str(obj.__code__))
            if file_name:
                file_name = file_name.groups()[0]
            if file_name:
                if import_modules:
                    file_name = file_name.groups()[0]
                    logger.debug("Adding %s.%s", file_name, obj.__name__)
                    return set([f"{file_name}.{obj.__name__}"])
                else:
                    logger.debug("I NEED just THE MODULE: %s", str(file_name))
                    return set([str(file_name)])
            else:
                if import_modules:
                    logger.debug("No filename parsed, use the module: %s", obj.__module__)
                    return set([obj.__module__])
                else:
                    logger.debug("No filename parsed, use the FQDN: %s", obj.__module__)
                    return set([f"{obj.__module__}.{obj.__name__}"])
        elif import_modules:
            logger.debug("%s %s missing __code__ < I need this module!", loc, obj)
        else:
            logger.debug("%s type_str=%s < I need this FQDN!", loc, type_str)


    elif "." in type_str:
        if import_modules:
            logger.debug("%s type_str=%s < I need this non-callable module!", loc, type_str)
        else:
            logger.debug("%s type_str=%s < I need this non-callable FQDN!", loc, type_str)
            parsed_type = re.match("<class '([^']+)'>", type_str)
            if parsed_type:
                parsed_type = parsed_type.groups()[0]
                if parsed_type and parsed_type.startswith("__main__"):
                    ext_module_file = inspect.getfile(obj.__class__)
                    logger.info(ext_module_file)
                    matched = re.search(r"([\w]+).py", ext_module_file)
                    if matched:
                        ext_module_file = matched.groups()[0]
                        logger.info(ext_module_file)
                        fqn = re.sub("__main__", ext_module_file, parsed_type)
                        logger.info(fqn)
                        return set([fqn])

                return set([parsed_type])

    if isinstance(obj, dict):
        for k,v in obj.items():
            #all_types.add(type(k))
            all_types |= get_all_types("6", v, import_modules)

    # Now handle all other iterables aside from dictionaries
    # Non-iterables will throw a TypeError but that's perfectly ok
    elif not isinstance(obj, str):
        try:
            for obj_i in obj:
                all_types |= get_all_types("7", obj_i, import_modules)
        except TypeError:
            pass

    result = set()
    for this_type in all_types:
        parsed_type = re.match("<class '([^']+)'>", str(this_type))
        if parsed_type:
            result_type = parsed_type.groups()[0]
            logger.debug("Adding %s", result_type)
            result.add(result_type)

    if result:
        logger.debug("result=%s", result)
    return result


def generate_all_tests_and_metadata_helper( local_all_metadata:dict,
                                            func_names:list,
                                            outdir:Path,
                                            tests_dir:Path,
                                            suffix:Path=Path(".json")):
    """
    This function generates units tests for decorated functions and methods.

    Because I also decorate functions within this very file
    (i.e. the functions and methods that implement the automatic unit
    test generation), it's necessary to call this function twice to
    ensure that unit tests are created for all functions and
    methods defined within this very file.

    I do claim this is self-testing code after all!
    """

    for func_name in func_names:
        logger.debug("func_name=%s", func_name)
        function_metadata:FunctionMetaData = copy.deepcopy(local_all_metadata[func_name])
        coverage_io_keys = copy.deepcopy(list(function_metadata.coverage_io.keys()))

        # TODO Fix bug here where function_metadata.coverage_io dictionaries
        # are shared for multiple functions within this file.
        # Patched for now by making a deep copy of each in the lines above,
        # but it feels hacky.
        purged = 0

        # TODO The below below is likely unnecessary now
        for timestamp in coverage_io_keys:
            if not set(function_metadata.coverage_io[timestamp]['Coverage']) & set(function_metadata.lines):
                purged += 1
                function_metadata.purge_record(timestamp)
                function_metadata.unified_test_coverage = set()

        if purged:
            for _, cov in function_metadata.test_coverage.items():
                function_metadata.unified_test_coverage |= set(cov)
            function_metadata.percent_covered = function_metadata.percent_covered(2)

        test_suite = function_metadata.coverage_io
        '''
        The json file is optional and unused but makes for
        friendly reading of the inputs to the unit test if
        the actual .py unit test file is hard to read
        due to formatting.
        '''
        this_func_name = re.sub(".__init__", ".constructor", func_name)
        filename = outdir.joinpath(f"{this_func_name}{suffix}")
        with open(filename, "w") as test_io_file:
            logger.info("Dumping test metadata to %s...", str(filename))
            json.dump(function_metadata, test_io_file, cls=FunctionMetaDataEncoder)

        auto_generate_tests(local_all_metadata[func_name],
                            test_suite,
                            func_name,
                            function_metadata.source_file,
                            tests_dir)
        local_all_metadata.pop(func_name)
    return local_all_metadata

@unit_test_generator_decorator(active)
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
    decorated with @unit_test_generator_decorator(active)!
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

        func_names = copy.deepcopy(list(all_metadata.keys()))
        local_all_metadata = all_metadata
        local_all_metadata = generate_all_tests_and_metadata_helper(local_all_metadata,
                                                                    func_names,
                                                                    outdir,
                                                                    tests_dir,
                                                                    suffix)

@unit_test_generator_decorator(active)
def update_global(obj: __builtins__, this_global:str, phase:str, state:dict):
    """
    Update and return state dictionary with new global.
    """
    if isinstance(obj, set):
        this_entry = sorted_set_repr(obj)
    else:
        this_entry = repr(obj)
    # The block below is for a separate project
    #if this_global == "g_function_params_write_locs":
        #logger.critical(f"{this_global=}\n{obj=}")
    if this_entry.startswith("<"):
        return state
    #print(f"{this_global}={this_entry}")

    if isinstance(obj, dict) and this_entry != "{}":
        state[phase]['globals'][this_global] = this_entry
    else:
        state[phase]['globals'][this_global] = this_entry
    return state




@unit_test_generator_decorator(active)
def normalize_arg(arg:typing.Any):
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
    if isinstance(arg, str) and arg[0] == '"' and arg[-1] == '"':
        arg = arg[1:-1]
    return arg

'''
import ast
from collections import namedtuple

Import = namedtuple("Import", ["module", "name", "alias"])

def get_imports(path):
    with open(path) as fh:
       root = ast.parse(fh.read(), path)

    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split('.')
        else:
            continue

        for n in node.names:
            yield Import(module, n.name.split('.'), n.asname)
'''
@unit_test_generator_decorator(active)
def coverage_str_helper(this_list:list, non_code_lines:set)->list:
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

@unit_test_generator_decorator(active)
def gen_coverage_list(  function_metadata:FunctionMetaData,
                        coverage_list:list,
                        func_name:str,
                        tab:str=" "*3):
    """
    Given a state[timestamp] and function name create a comment string
    to show lines covered, percent covered, and lines not covered
    """
    first_source_line_num = function_metadata.lines[0]
    last_source_line_num = function_metadata.lines[-1]
    range_source_line_nums =   set([x for x in range(first_source_line_num,
                                                     last_source_line_num+1)
                                    ])
    coverage_set = set(coverage_list)
    coverage_list = sorted(list(range_source_line_nums & coverage_set))
    if not coverage_list:
        logger.warning("Fix the bug here; no coverage for %s", func_name)
        return []
    non_code_lines = function_metadata.return_non_code_lines()

    logger.debug("coverage_list=%s", coverage_list)
    logger.debug("range_source_line_nums=%s", range_source_line_nums)
    logger.debug("func_name=%s", func_name)
    if logger.level >= logging.DEBUG:
        msg = pp.pformat(function_metadata.lines)
        logger.debug("lines=\n%s", msg)

    percent_covered = 100*len(coverage_list)/len(function_metadata.lines)
    #percent_covered = 100*percent_covered
    coverage_str_list = []
    start = []
    start.append(f"{tab}# Coverage: {percent_covered:.2f}% of function lines ")
    start.append(f"[{first_source_line_num}-{last_source_line_num}]\n")
    start.append(f"{tab}# Covered Lines: ")
    start = ''.join(start)
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

@unit_test_generator_decorator(active)
def meta_program_function_call( this_state:dict,
                                timeframe:str,
                                tab:str,
                                package,
                                func_name:str,
                                result_type:str):
    """
    Given the provided arguments,
    return a list of valid Python code that executes the decorated
    function and asserts that the result is as expected.
    """
    class_var_name = ""
    is_method = False
    test_str_list = []

    # Handle the case that decoratee is a
    # class method by constructing the class
    if "Constructor" in this_state:
        func_name=func_name.split('.')[1]
        class_var_name = "this_class"
        is_method = True # Marginally faster than this string compare?
        line = f"{tab}{class_var_name} = {this_state['Constructor']}\n"
        test_str_list.append(line)

    kwargs_str = ''
    # TODO: Test this block below
    if 'kwargs' in this_state[timeframe]:
        # Creating "line" variable to condense line width
        line = f"{tab}kwargs = {this_state[timeframe]['kwargs']}\n"
        test_str_list.append(line)
        kwargs_str = ", kwargs=kwargs)"
        #line = f"{tab}x = {package}.{func_name}(*args, kwargs=kwargs)\n"
        #test_str_list.append(line)

    assignment = f"{tab}x = "
    call = ""
    if is_method:
        call = f"{class_var_name}.{func_name}(*args{kwargs_str})\n"
    else:
        call = f"{package}.{func_name}(*args{kwargs_str})\n"

    if 'Exception' in this_state:
        e_type = this_state['Exception']['Type']
        e_type =  re.search("<class '([^']+)'", e_type).groups()[0]
        e_str = this_state['Exception']['message']
        # Any special chars, e.g. an empty list: [] in the e_str will break
        # the pytest.raise() parser, so use re.escape()
        e_str = re.escape(e_str)

        # Source: https://docs.pytest.org/en/6.2.x/assert.html#assertraises
        line = f'{tab}with pytest.raises({e_type}, match=r\"{e_str}\"):\n'
        test_str_list.append(line)
        line = f'{tab*2}{call}'
        test_str_list.append(line)
    else:
        normal_call = f"{assignment}{call}"
        if func_name.endswith(".__init__"):
            #func_name = re.sub(".__init__", "", func_name)
            normal_call = re.sub(".__init__", "", normal_call)
        test_str_list.append(normal_call)
        if not this_state['Result']:
            line = f"{tab}assert not x\n"
        else:
            result_str = ""
            logger.debug("func_name=%s", func_name)
            if result_type == "str":
                logger.debug("String: %s", this_state)
                x = this_state['Result'].replace("'", "\\'").replace('"', '\\"')
                result_str = f"\'{x}\'"
            else:
                logger.debug("Not string")
                result_str = this_state['Result']
                result_str = normalize_arg(this_state['Result'])
            assert not result_str.startswith("'\n"), "Bad juju"
            #line = f"{tab}assert x == {result_str}\n"
            if func_name.endswith(".__init__"):
                class_fqn = re.sub(".__init__.*$", "", call)
                line = f"{tab}assert isinstance(x, {class_fqn})\n"
            else:
                line = f"{tab}assert x == {result_str}\n"
        test_str_list.append(line)
    return test_str_list

@unit_test_generator_decorator(active)
def auto_generate_tests(function_metadata:FunctionMetaData,
                        state:dict, func_name:str, source_file:Path,
                        tests_dir:Path, indent_size:int=2):
    """
    This is the function that can automatically create a unit
    test file for each decorated function.
    The contents of the unit test file(s) are created by appending
    to lists of strings, these lists of strings are evenutally
    written to a file, one per decorated function.
    """
    imports = []
    was_executed = False
    # TODO Add to the import list any specific modules for
    # which repr doesn't work, e.g.
    # imports.append(import pandas as pd\n")

    tab = " "*indent_size
    header = []
    pct = function_metadata.coverage_percentage
    #assert pct <= 100, "Bad math"
    line = f"{tab}# In sum, these tests covered {pct}% of {func_name}'s lines\n"
    header.append(line)
    if pct < 100:
        uncovered_str = function_metadata.get_all_uncovered_line_str()
        lines = [
                    f"{tab}# Line(s) not covered by ANY of the tests below:\n",
                    f"{tab}# {uncovered_str}\n"
                ]
        header += lines

    test_str_list_def_dict = defaultdict(int)
    # Only functions/methods that accessed global
    # variables will need to be patched
    # The variable below will help us keep track of this.
    needs_monkeypatch = False
    package = Path(source_file).stem
    initial_import = get_module_import_string(source_file).split(".")
    initial_import_prefix = ".".join(initial_import[:-1])
    initial_import_suffix = initial_import[-1]
    if initial_import_prefix:
        initial_import = f"from {initial_import_prefix} import {initial_import_suffix}\n"
    elif initial_import_suffix:
        initial_import = f"import {initial_import_suffix}\n"
    else:
        initial_import = ""

    item = "globals"
    for timestamp_index, timestamp in enumerate(sorted(state)):
        test_str_list = [f"def test_{func_name.replace('.','_')}_{timestamp_index}():\n",
                         f"{tab}monkeypatch = MonkeyPatch()\n"]
        monkey_patches = []
        coverage_list = gen_coverage_list(  function_metadata,
                                            state[timestamp]["Coverage"],
                                            func_name,
                                            tab)
        # Due to some complexity of self-testing (e.g. bugs I can't yet squash)
        # coverage_str might be empty.  That's fine, so continue
        if not coverage_list:
            continue
        coverage_str = ''.join(coverage_list)
        test_str_list.append(coverage_str)
        #test_str_list += f'{tab}# Coverage: {state[timestamp]["Coverage"]}\n'

        #print(f"{state[timestamp].keys()}")
        timeframe = "Before"
        item = "globals"
        for k in sorted(state[timestamp][timeframe][item]):
            needs_monkeypatch = True
            v = state[timestamp][timeframe][item][k]
            v = normalize_arg(v)
            test_str_list.append(f"{tab}{k} = {v}\n")
            line = f'{tab}monkeypatch.setattr({package}, \"{k}\", {k})\n'
            monkey_patches.append(line)
        if monkey_patches:
            test_str_list += monkey_patches
        #monkey_patches = []
        test_str_list.append(f"{tab}args = []\n")
        is_method = function_metadata.is_method
        logger.debug("%s is method: %s", func_name, is_method)

        # Remove the 'self' argument from the arg list if this
        # decoratee is a class method (as opposed to a regular function)
        """
        if function_metadata.is_method:

            args = state[timestamp][timeframe]['args'][1:]
            if "gas" in function_metadata.name:
                logger.critical("args=%s", args)
            state[timestamp][timeframe]['args'] = args
            if function_metadata.name == "gas":
                logger.critical("args=%s", args)
        """

        for arg in state[timestamp][timeframe]['args']:
            # TODO If an arg is a class, construct it
            #if not isinstance(arg, str):
            #    unpacked_args.append(f"{arg}")
            #else:
            #    unpacked_args.append(arg)
            test_str_list.append(f"{tab}args.append({arg})\n")
        #logger.debug("unpacked_args=%s", unpacked_args)
        #unpacked_args = ','.join(unpacked_args)

        this_result_type = function_metadata.result_types[timestamp]
        test_str_list += meta_program_function_call(state[timestamp],
                                                        timeframe,
                                                        tab,
                                                        package,
                                                        func_name,
                                                        this_result_type)
        timeframe = "After"
        item = "globals"
        dict_get = ".__dict__.get"
        for k in sorted(state[timestamp][timeframe][item]):
            v = state[timestamp][timeframe][item][k]
            v = normalize_arg(v)

            if v in ['None', '[]', '{}']:
                line = f'{tab}assert not {package}{dict_get}(\"{k}\")\n'
                line = re.sub("<class '([^']+)'>", "\\1", line)
                test_str_list.append(line)
                needs_monkeypatch = True
                continue

            # Define a local variable with the
            # same name and valueas to one being asserted
            test_str_list.append(f"{tab}modified_{k} = {v}\n")
            # Now assert that that variable exists in the global namespace
            line = f'{tab}assert {package}{dict_get}(\"{k}\") == modified_{k}\n'
            line = re.sub("<class '([^']+)'>", "\\1", line)
            test_str_list.append(line)
            needs_monkeypatch = True



        # What if a global variable is written to but not read from?
        # handle that here, otherwise I'd have to put this code in the loop above
        if not needs_monkeypatch:
            test_str_list[1] = ""

        #test_str_list += monkey_patches
        # Delete all references to "__main__", it's needless
        #print(test_str_list)
        test_str_list = [re.sub("__main__.", "", x) for x in test_str_list]
        if not test_str_list:
            # If this function was never executed, its coverage is 0%
            # Raise an exception to alert the user
            # Note that we don't need any imports at all
            test_str_list.append(f"{tab}raise Exception('Empty test - this function was never executed')")

        if test_str_list:
            test_str_list_def_dict[timestamp_index] = test_str_list
            was_executed = True

    # End of loop over all samples

    if was_executed:
        imports.append(initial_import)

    if function_metadata.needs_pytest:
        imports.append("import pytest\n")

    # Only functions/methods that access
    # global variables will need to be patched
    if needs_monkeypatch:
        imports.append("from _pytest.monkeypatch import MonkeyPatch\n")

    custom_imports = []
    logger.debug("func_name=%s\nfunction_metadata.types_in_use=%s", func_name, function_metadata.types_in_use)
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
        imports.append(f"# Now import modules specific to {func_name}:\n")
    imports += custom_imports

    logger.debug("func_name=%s", func_name)
    result_file_str = f"test_{func_name}.py"#.replace('.','_')}.py"
    result_file_str = re.sub("__init__", "constructor", result_file_str)
    result_file = tests_dir.joinpath(result_file_str)


    #final_result = ''.join(y for y in x for x in test_str_list_def_dict.values())
    #print(final_result)
    #final_result_bytes = "".join([x for x in final_result]).encode()
    #logger.critical(final_result)

    if "pytest" in sys.modules:
        """
        Return hash of resulting string here,
        this is used when self-testing auto_generate_tests with
        unit_test_generator_decorator
        """
        h = hashlib.new('sha256')
        h.update(str(sorted(test_str_list_def_dict.items())).encode())
        return h.digest().hex()
        #return str(sorted(test_str_list_def_dict.items()))#final_result_bytes

    with open(result_file, "w") as st:
        for list in [imports, header]:
            if list:
                st.writelines(list)
        for list in test_str_list_def_dict.values():
            st.writelines(list)

    logger.info("Wrote to %s", result_file)

    # Format the generated Python file with black for easier reading

    try:
        subprocess.run( f"black {result_file}".split(),
                        check=True,
                        capture_output=True
                        )
    except CalledProcessError as e:
        logger.error("Got Error running black formatter on %s:", result_file)
        logger.error(pp.pformat(e)+"\n")
        logger.error(e.stderr.decode()+"\n")
        if e.stdout:
            logger.error(e.stdout.decode())

    logger.info("Re-formatted %s with black formatter", result_file)

    # Return hash of resulting string here
    h = hashlib.new('sha256')
    h.update(str(sorted(test_str_list_def_dict.items())).encode())
    return h.digest().hex()
