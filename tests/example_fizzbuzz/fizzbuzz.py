from src.unit_test_generator import unit_test_generator_decorator,\
                                generate_all_tests_and_metadata
from pathlib import Path

mode = 'fizzbuzz'

@unit_test_generator_decorator
def fizzbuzz(number: int):
    """
    An intentionally sub-optimal
    function for demonstration.

    This function acts as 'fizzbuzz' if the "mode"
    global variable equals the string 'fizzbuzz'.

    If the "mode" global variable is 'buzzfizz',
    the logic for numbers 3 and 5 is swapped, and
    'buzzfizz' is the expected string for numbers
    divisible by 15.

    An error string is returned for any "mode"
    value not in ['fizzbuzz', 'buzzfizz']
    """
    result = ""
    if mode == 'fizzbuzz':
        if 0 == number % 3:
            result = f"{number:<2} with {mode=} yields 'fizz'"
        if 0  == number % 5:
            result = f"{number:<2} with {mode=} yields 'buzz'"
        if 0 == number % 15:
            result = f"{number:<2} with {mode=} yields 'fizzbuzz'"
    elif mode == 'buzzfizz':
        if 0 == number % 3:
            result = f"{number:<2} with {mode=} yields 'buzz'"
        if 0  == number % 5:
            result = f"{number:<2} with {mode=} yields 'fizz'"
        if 0 == number % 15:
            result = f"{number:<2} with {mode=} yields 'buzzfizz'"
    else:
       result = f"Mode '{mode}' invalid for blackbox()"
    return result
# Begin ad hoc tests
print(fizzbuzz(6))
print(fizzbuzz(30))
mode = 'buzzfizz'
print(fizzbuzz(45))
print(fizzbuzz(9))
mode = "a_test"
print(fizzbuzz(60))

"""
The generate_all_tests_and_metadata() function takes 2 Paths:
1. The output directory for the unit tests (.py)
2. The output directory for the .json files (I/O for each test)
"""
generate_all_tests_and_metadata(Path('.'), Path('.'))
