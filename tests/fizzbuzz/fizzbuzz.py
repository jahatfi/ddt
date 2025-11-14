"""
Test case to demonstrate the DDT concept on a variant of the fizzbuzz problem.
Includes a global variable.
"""

from src import unit_test_generator
from src.unit_test_generator import (
    generate_all_tests_and_metadata,
    unit_test_generator_decorator,
    Capturing
)

mode = 'fizzbuzz' # pylint: disable=invalid-name


@unit_test_generator_decorator(110,100)
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
        result = f"Mode '{mode}' invalid for fizzbuzz()"
    return result
