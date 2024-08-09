import copy
import logging
from pathlib import Path
from typing import Callable
from src import unit_test_generator
from src.unit_test_generator import (
    unit_test_generator_decorator,
    generate_all_tests_and_metadata
)



def outermost_decorator_with_parameters(my_int: int):
    def my_outer_decorator_with_args(f:Callable):
        def innermost_decorator(*args, **kwargs):
            print(f"Before call to '{f.__name__}'")
            print(f"{args=}; {my_int=}")
            args_copy = list(copy.deepcopy(args))
            args_copy[0] = args_copy[0] + 1
            args = tuple(args_copy)
            print(f"Modified args: {args=}")
            result = f(*args, **kwargs)
            print(f"After call: {result=}")
            return result
        return innermost_decorator
    return my_outer_decorator_with_args

#@outermost_decorator_with_parameters(5)
@unit_test_generator_decorator(percent_coverage=100)
def add_ints(a: int, b:int)->int:
    return a+b+c[0]

c = [5] # global variable
x = 2
y = 7
print(f"Adding {x},{y},{c}...")
final_result = add_ints(x, y)
print(f"The result is {final_result}")

generate_all_tests_and_metadata(Path('.'), Path('.'))