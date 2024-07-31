import copy
from typing import Callable
from ...src.unit_test_generator import unit_test_generator_decorator

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
            print(f"In decorator after call: {result=}")
            return result
        return innermost_decorator
    return my_outer_decorator_with_args

@outermost_decorator_with_parameters(5)
def add_ints(a: int, b:int)->int:
    return a+b+c[0]

c = [5] # global variable
x = 2
y = 7
print(f"Adding {x},{y},{c}...")
final_result = add_ints(x, y)
print(f"{final_result=}")
