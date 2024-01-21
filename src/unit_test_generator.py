import re
import os
import sys
import json
import copy
import time
import types
import inspect
import pprint
import logging
import coverage
import subprocess
import pandas as pd

from dis import dis
from io import StringIO
from functools import wraps
# NOTE: WindowsPath is in fact required is running on Windows!
from pathlib import Path, WindowsPath
from json import JSONEncoder
from collections import defaultdict
from subprocess import CalledProcessError
from types import MappingProxyType

pp = pprint.PrettyPrinter(indent=3)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set this value to disable the
# unit_test_generator_decorator once coverage hits
# this value as a percent, e.g. 80 = 80% coverage
coverage_cutoff = 100
recursion_depth_per_decoratee = defaultdict(int)

def unit_test_generator_decorator(func:callable):
    """
    Any function wrapped with this decorator will have
    it's execution coverage saved as though under a unit test.
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
        global recursion_depth_per_decoratee
        if "pytest" in sys.modules:
            logger.debug("pytest is loaded; don't decorate when under a test")
            result = func(*args, **kwargs)
            #logger.critical(f"Undecorating {func_name}".center(80, '-'))
            return result

        function_calls = None
        function_calls = defaultdict(int)

        for f in inspect.stack()[::-1]:
            F = inspect.getframeinfo(f[0])
            function_calls[F.function] += 1
        if func.__name__ not in recursion_depth_per_decoratee:
            #logger.critical(f"{func.__name__} Not found in {all_metadata.keys()=}")
            recursion_depth_per_decoratee[func.__name__] = max(function_calls.values())

        elif 1 < max(function_calls.values()) >= recursion_depth_per_decoratee[func.__name__]:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.critical(e)
                raise e
        try:
            result = do_the_decorator_thing(func, *args, **kwargs)
            return result
        except Exception as e:
            logger.warning(f"{e=}")
            raise e
    return unit_test_generator_decorator_inner

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

@unit_test_generator_decorator
def sorted_set_repr(obj: set):
    """
    I want sets to appear sorted when initialized in unit tests.
    Thus function does just that.
    """

    obj = sorted(list(obj))
    # 2. Convert the list to valid Python code
    obj = repr(obj)
    # Replace the square brackets (list) to curly braces (set)
    obj = f"{{{obj[1:-1]}}}"
    # "obj" is now valid Python code that will create a set.
    # The objects in this line of code appear in sorted order
    return repr(obj)

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
    it's execution coverage saved as though under a unit test.
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
        logger.debug(f"{func_name} has source line #s: {min(x)}-{max(x)}")

    elif func_name in all_metadata:
        this_metadata = all_metadata.pop(func_name)



    state = {   "Before":{'globals':dict()},
                "After":{'globals':dict()},
            }

    #args_copy = [convert_to_serializable(x) for x in args]
    args_copy = []

    if this_metadata.is_method:
        state['Constructor'] = args[0].repr()

    new_types_in_use = set()
    for arg in args:
        new_types_in_use |= get_all_types("1", arg, False)
        if hasattr(arg, "__dict__"):
            for v in arg.__dict__.values():
                new_types_in_use |= get_all_types("1.1", v, False)
        if callable(arg):
            logger.debug(f"{func_name} decorator got {arg.__module__}.{arg.__qualname__} as callable")
            if arg.__module__ == "__main__":
                file_name = re.search(r"([\w]+).py", str(arg.__code__))
                if file_name:
                    file_name = file_name.groups()[0]
                    logger.debug(f"{file_name}.{arg.__name__}")
                    args_copy.append(f"{file_name}.{arg.__name__}")
                else:
                    logger.critical(f"NO FILENAME FOUND!: {re.escape(str(arg.__code__))=}")
            #logger.critical(dir(arg))
            #logger.critical(arg.__module__)
            else:
                logger.critical(arg.__qualname__)
                args_copy.append(arg.__qualname__)
                #this_metadata.types_in_use.add(f"{arg.__module__}.{arg.__name__}")

            #sys.exit(1)
        elif not isinstance(arg, str):
            type_str = str(type(arg))
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
                    logging.debug(f"Possible bug here for update_global: {class_repr=}")
                #logger.debug(f"Got class!: {class_repr}")
                try:
                    eval(class_repr)
                    args_copy.append(class_repr)
                except SyntaxError as e:
                    # skip on error
                    logger.debug(f"Got {type(e)} decorating {func_name} repr'ing {arg=}:\n{e}")
                    x = func(*args, **kwargs)
                    all_metadata[func_name] = this_metadata
                    return x
            else:
                #logger.critical(f"repr arg: {arg} {type(arg).__module__=}")
                args_copy.append(repr(arg))
        else:
            args_copy.append("\""+re.sub(r"(?<!\\) \"", r'\\"',arg)+"\"")
        #if "__main__" in args_copy[-1] and "at_index" in args_copy[-1]:
        #    logger.critical(args_copy)
    if len(args) != len(args_copy):
        logger.critical(f"{args=} != {args_copy=}")

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

    cov_report_ = None
    timestamp = None
    result = None
    data_file = f"coverage_{func_name}_{time.perf_counter()}"
    cov = coverage.Coverage(data_file)
    with cov.collect():
        try:
            if kwargs:
                state['Before']['kwargs'] = kwargs
                result = func(*args, **kwargs)
            else:
                result = func(*args)
            logger.debug("No exception :)")
        except Exception as e:
            #this_metadata.exceptions[timestamp] = e
            logger.debug(f"Caught {e=}")
            caught_exception = e
            #raise caught_exception
    with Capturing() as stdout_lines:
        cov.json_report(outfile='-')
    # result will not exist if the function threw an exception
    #logger.debug(f"{type(result)=}, {result=}")
    cov_report_ = json.loads(stdout_lines[0])
    timestamp = f"{func_name}_{time.time_ns()}"#cov_report_['meta']['timestamp']
    if caught_exception:
        logger.debug(f"{caught_exception=} @ {timestamp} {result=}")

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
    #logger.critical(f"{this_coverage=}")
    is_subset = False
    Path.unlink(Path(data_file))

    # If no new lines were covered, do nothing else,
    # but just immediately return the result

    pct_covered = this_metadata.percent_covered()
    pct_covered = round(pct_covered, 4)
    delta = len(this_coverage-this_metadata.unified_test_coverage)

    if delta == 0:
        all_metadata[func_name] = this_metadata
        logger.debug(f"No new coverage decorating {func_name}; skipping.")
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
            logger.debug(f"{source_file}: discarding current test.")
            is_subset = True
            break
        # Discard all previous tests that covered a smaller subset
        # of the lines covered by this test
        if prev_coverage.issubset(this_coverage):
            logger.debug(f"{source_file} removing subset coverage @ {key}.")
            this_metadata.test_coverage.pop(key)


    # Put another way, only keep these results IF the test coverage
    # here is NOT a subset of ANY previous run
    if is_subset:
        all_metadata[func_name] = this_metadata
        if caught_exception:
            raise caught_exception
        else:
            logger.debug(f"{func_name} coverage is a subset {this_metadata.coverage_percentage=}")
            #logger.critical(f"Undecorating {func_name}".center(80, '-'))
            return result

    logger.debug(f"{func_name} coverage @{timestamp} is not a subset")

    if caught_exception:
        logger.debug(f"{caught_exception=}")
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
        #print("State['Result']:")
        #pp.pprint(state['Result'])
    #logger.debug(f"{result_type} {type(result)=} {result=}")
    #assert result_type == type(result), f"{result_type} {type(result)} type or result changed!"

    phase = "After"
    for this_global in this_metadata.global_vars_written_to:
        obj = func.__globals__[this_global]
        state = update_global(obj, this_global, phase, state)
        these_types = get_all_types("5", func.__globals__[this_global])
        this_metadata.types_in_use |= these_types

    this_metadata.unified_test_coverage |= this_coverage
    percent_covered = this_metadata.percent_covered(2)

    logger.debug(f"Achieved {percent_covered}% for {func_name}")
    sorted_coverage = sorted(list(this_coverage))
    logger.debug(f"{sorted_coverage=}")
    # TODO remove these assserts and the timestamps set
    assert set(sorted_coverage) & set(this_metadata.lines)
    state["Coverage"] = sorted_coverage
    assert not timestamp in timestamps
    timestamps.add(timestamp)
    this_metadata.coverage_percentage = percent_covered
    # TODO remove this deepcopy
    this_metadata.coverage_io[timestamp] = copy.deepcopy(state)
    this_metadata.coverage_cost[timestamp] = count_objects(state)
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
        logger.critical(f"{obj=}")
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
                    coverage_cost:dict = None,
                    coverage_io:dict = None,
                    coverage_percentage:float=0.0,
                    result_types:dict = None,
                    test_coverage:dict = None,
                    types_in_use:set = None,
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
        self.coverage_cost = {} if coverage_cost == None else coverage_cost
        self.coverage_io = {} if coverage_io == None else coverage_io
        self.coverage_percentage = coverage_percentage
        self.result_types = {} if result_types == None else result_types
        self.test_coverage = {} if test_coverage == None else test_coverage
        self.types_in_use = set() if types_in_use == None else types_in_use
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
        logger.debug(f"{uncovered=} {self.non_code_lines=}")
        if uncovered:
            result = coverage_str_helper(list(uncovered), self.non_code_lines)
        else:
            result = uncovered
        logger.debug(f"{result}")
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
        #logger.critical(f"{result=}")
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
                logger.error(f"Failed to pop key {e}")
        # TODO call self.update_types_in_use here

    def default(self):
        logger.critical("DIggity")
        return _default()

    # https://stackoverflow.com/questions/3768895
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

# https://pynative.com/make-python-class-json-serializable/
class FunctionMetaDataEncoder(JSONEncoder):
    def default(self, o) ->str:
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
        logger.debug(f"Got import for {func_name} {this_global=}")
    return is_variable

@unit_test_generator_decorator
def return_function_line_numbers_and_accessed_globals(f: callable):
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
    logger.debug(f"{f=} {type(f)=}")
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

@unit_test_generator_decorator
def count_objects(obj: any):
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

def get_all_types(loc: str, obj:any, import_modules:bool=True)->set:
    """
    Return the set of all types contained in this object,
    It might be a list of sets so return {"list", "set"}
    """
    all_types = set()
    type_str = str(type(obj))
    type_list =  ['str', 'int', 'list', 'set', 'dictionry', 'dict']
    if not any(x in type_str for x in type_list):
        logger.debug(f"{loc} {type_str=}")
    if callable(obj):
        if hasattr(obj, "__code__"):
            logger.debug(f"{loc} {obj.__module__}.{obj.__name__} as callable")
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
                    logger.debug(f"Adding {file_name}.{obj.__name__}")
                    return set([f"{file_name}.{obj.__name__}"])
                else:
                    logger.debug(f"I NEED jusT THE MODULE: {str(file_name)}")
                    return set([str(file_name)])
            else:
                if import_modules:
                    logger.debug(f"No filename parsed, use the module: {obj.__module__}")
                    return set([obj.__module__])
                else:
                    logger.debug(f"No filename parsed, use the FQDN: {obj.__module__}")
                    return set([f"{obj.__module__}.{obj.__name__}"])
        elif import_modules:
            logger.debug(f"{loc} {obj} missing __code__ < I need this module!")
        else:
            logger.debug(f"{loc} {type_str=} < I need this FQDN!")


    elif "." in type_str:
        if import_modules:
            logger.debug(f"{loc} {type_str=} < I need this non-callable module!")
        else:
            logger.debug(f"{loc} {type_str=} < I need this non-callable FQDN!")
            parsed_type = re.match("<class '([^']+)'>", type_str)
            if parsed_type:
                return set([parsed_type.groups()[0]])

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
            logger.debug(f"Adding {result_type}")
            result.add(result_type)

    if result:
        logger.debug(f"{result=}")
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
        logger.debug(f"{func_name=}")
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
        filename = outdir.joinpath(f"{func_name}{suffix}")
        with open(filename, "w") as test_io_file:
            logger.info(f"Dumping test metadata to {str(filename)}...")
            json.dump(function_metadata, test_io_file, cls=FunctionMetaDataEncoder)

        auto_generate_tests(local_all_metadata[func_name],
                            test_suite,
                            func_name,
                            function_metadata.source_file,
                            tests_dir)
        local_all_metadata.pop(func_name)
    return local_all_metadata

@unit_test_generator_decorator
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
        logger.debug(f"{phase=}")
        #pp.pprint(all_metadata)

        logger.debug(f"{phase}: {all_metadata.keys()=}")

        func_names = copy.deepcopy(list(all_metadata.keys()))
        local_all_metadata = all_metadata
        local_all_metadata = generate_all_tests_and_metadata_helper(local_all_metadata,
                                                                    func_names,
                                                                    outdir,
                                                                    tests_dir,
                                                                    suffix)

@unit_test_generator_decorator
def update_global(obj: any, this_global:str, phase:str, state:dict):
    """
    Update and return state dictionary with new global.
    """
    #logger.debug(f"{this_global=}\n{func.__globals__[this_global]}")
    if isinstance(obj, set):
        this_entry = sorted_set_repr(obj)
    else:
        this_entry = repr(obj)
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




@unit_test_generator_decorator
def normalize_arg(arg:any):
    """
    Convert arg to "canonical" form; i.e. convert it to a string format such
    that by writing it to a file it become proper Python code.
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
@unit_test_generator_decorator
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
            logger.critical(f"Invalid coverage! {this_list}")

    return results_list

@unit_test_generator_decorator
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
    #logger.critical(f"{func_name} {coverage_list=}")
    coverage_list = set(coverage_list)
    coverage_list = sorted(list(range_source_line_nums & coverage_list))
    if not coverage_list:
        logger.warning(f"Fix the bug here; no coverage for {func_name}")
        return []
    non_code_lines = function_metadata.return_non_code_lines()

    logger.debug(f"{coverage_list=}")
    logger.debug(f"{range_source_line_nums=}")
    logger.debug(f"{func_name=}")
    if logger.level >= logging.DEBUG:
        msg = pp.pformat(function_metadata.lines)
        logger.debug(f"lines=\n{msg}")

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

@unit_test_generator_decorator
def meta_program_function_call( this_state:dict,
                                timeframe:str,
                                tab:str,
                                file_stem,
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
        #line = f"{tab}x = {file_stem}.{func_name}(*args, kwargs=kwargs)\n"
        #test_str_list.append(line)

    assignment = f"{tab}x = "
    call = ""
    if is_method:
        call = f"{class_var_name}.{func_name}(*args{kwargs_str})\n"
    else:
        call = f"{file_stem}.{func_name}(*args{kwargs_str})\n"

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
        test_str_list.append(normal_call)
        if not this_state['Result']:
            line = f"{tab}assert not x\n"
        else:
            result_str = ""
            logger.debug(f"{func_name=}")
            if result_type == "str":
                logger.debug(f"String: {this_state=}")
                x = this_state['Result'].replace("'", "\\'").replace('"', '\\"')
                result_str = f"\'{x}\'"
            else:
                logger.debug("Not string")
                result_str = this_state['Result']
                result_str = normalize_arg(this_state['Result'])
            assert not result_str.startswith("'\n"), "Bad juju"
            line = f"{tab}assert x == {result_str}\n"
            line = re.sub("<class '([^']+)'>", "\\1", line)
        test_str_list.append(line)
    return test_str_list

@unit_test_generator_decorator
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
    tab = " "*indent_size
    header = [f"def test_{func_name.replace('.','_')}():\n"]
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
    test_str_list = []
    test_str_list_2 = []
    # Only functions/methods that accessed global
    # variables will need to be patched
    # The variable below will help us keep track of this.
    needs_monkeypatch = False
    file_stem = Path(source_file).stem
    #logger.critical(state)
    for timestamp in sorted(state):
        #logger.critical(f"{func_name=} {timestamp=}")
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
            line = f'{tab}monkeypatch.setattr({file_stem}, \"{k}\", {k})\n'
            test_str_list_2.append(line)
        test_str_list += test_str_list_2
        test_str_list_2 = []
        test_str_list += f"{tab}args = []\n"
        is_method = function_metadata.is_method
        logger.debug(f"{func_name} is method: {is_method}")

        # Remove the 'self' argument from the arg list if this
        # decoratee is a class method (as opposed to a regular function)
        if function_metadata.is_method:
            args = state[timestamp][timeframe]['args'][1:]
            state[timestamp][timeframe]['args'] = args

        for arg in state[timestamp][timeframe]['args']:
            # TODO If an arg is a class, construct it
            #if not isinstance(arg, str):
            #    unpacked_args.append(f"{arg}")
            #else:
            #    unpacked_args.append(arg)
            test_str_list += f"{tab}args.append({arg})\n"
        #logger.debug(f"{unpacked_args=}")
        #unpacked_args = ','.join(unpacked_args)

        this_result_type = function_metadata.result_types[timestamp]
        test_str_list += meta_program_function_call(state[timestamp],
                                                    timeframe,
                                                    tab,
                                                    file_stem,
                                                    func_name,
                                                    this_result_type)
        timeframe = "After"
        item = "globals"
        dict_get = ".__dict__.get"
        for k in sorted(state[timestamp][timeframe][item]):
            v = state[timestamp][timeframe][item][k]
            v = normalize_arg(v)

            if v in ['None', '[]', '{}']:
                line = f'{tab}assert not {file_stem}{dict_get}(\"{k}\")\n'
                line = re.sub("<class '([^']+)'>", "\\1", line)
                test_str_list.append(line)
                needs_monkeypatch = True
                continue

            # Define a local variable with the
            # same name and valueas to one being asserted
            test_str_list.append(f"{tab}modified_{k} = {v}\n")
            # Now assert that that variable exists in the global namespace
            line = f'{tab}assert {file_stem}{dict_get}(\"{k}\") == modified_{k}\n'
            line = re.sub("<class '([^']+)'>", "\\1", line)
            test_str_list.append(line)
            needs_monkeypatch = True

    # What if a global variable is written to but not read from?
    # handle that here, otherwise I'd have to put this code in the loop above
    if needs_monkeypatch:
        header.append(f"{tab}monkeypatch = MonkeyPatch()\n")

    imports = []
    # TODO Add to the import list any specific modules for
    # which repr doesn't work, e.g.
    # imports.append(import pandas as pd\n")

    test_str_list += test_str_list_2
    # Delete all references to "__main__", it's needless
    test_str_list = [re.sub("__main__.", "", x) for x in test_str_list]
    if not test_str_list:
        # If this function was never executed, its coverage is 0%
        # Raise an exception to alert the user
        # Note that we don't need any imports at all
        test_str_list.append(f"{tab}raise Exception('Empty test - this function was never executed')")
    else:
        # TODO: This block feels messy; clean it up if possible
        # Convert the relative path to the source file to a proper python import
        rel_path = os.path.relpath(source_file, ".")
        # Replace all slashes with periods after dropping any leading "../"
        # Windows uses backslashes
        rel_path = re.sub(r"\.\.\\", "", rel_path)
        # Other other OS's use forward slashes
        rel_path = re.sub(r"\.\./", "", rel_path)
        # Windows uses backslashes
        rel_path = re.sub(r"\\", ".", rel_path)
        # Other other OS's use forward slashes
        rel_path = re.sub(r"/", ".", rel_path)
        # Trim off the trailing ".py"
        if rel_path.endswith(".py"):
            rel_path = rel_path[:-3]
        rel_path = rel_path.split('.')
        file_stem = '.'.join(rel_path[:-1])
        suffix = rel_path[-1]
        this_import = None
        if file_stem:
            this_import = f"from {file_stem} import {suffix}\n"
        else:
            this_import = f"import {rel_path[0]}\n"
        imports.append(this_import)

    if function_metadata.needs_pytest:
        imports.append("import pytest\n")

    # Only functions/methods that access
    # global variables will need to be patched
    if needs_monkeypatch:
        imports.append("from _pytest.monkeypatch import MonkeyPatch\n")

    custom_imports = []
    logger.debug(f"{func_name=}\n{function_metadata.types_in_use}")
    for this_type in function_metadata.types_in_use:
        splits = this_type.split(".")
        prefix = '.'.join(splits[:-1])
        suffix = splits[-1]
        if not suffix:
            logger.error("NO SUFFIX")
            continue
        if prefix == "__main__":
            custom_imports.append(f"from {file_stem} import {suffix}\n")
        elif prefix:
            custom_imports.append(f"from {prefix} import {suffix}\n")
        elif suffix:
            custom_imports.append(f"import {suffix}\n")

    if custom_imports:
        imports.append("\n")
        imports.append(f"# Now import modules specific to {func_name}:\n")
    imports += custom_imports

    logger.debug(f"{func_name=}")
    result_file = tests_dir.joinpath(f"test_{func_name.replace('.','_')}.py")
    final_result = test_str_list
    final_result = "".join([x for x in final_result]).encode()
    #logger.critical(final_result)

    if "pytest" in sys.modules:
        """
        Return hash of resulting string here,
        this is used when self-testing auto_generate_tests with
        unit_test_generator_decorator
        """
        return final_result

    with open(result_file, "w") as st:
        for list in [imports, header, test_str_list]:
            if list:
                st.writelines(list)

    logger.info(f"Wrote to {result_file}")

    # Format the generated Python file with black for easier reading

    try:
        subprocess.run( f"black {result_file}".split(),
                        check=True,
                        capture_output=True
                        )
    except CalledProcessError as e:
        logger.error(f"Got Error running black formatter on {result_file}:")
        logger.error(pp.pformat(e))
        logger.error(f"\n{e.stderr.decode()}")
        if e.stdout:
            logger.error(f"\n{e.stdout.decode()}")

    logger.info(f"Re-formatted {result_file} with black formatter")

    # Return hash of resulting string here
    return final_result
