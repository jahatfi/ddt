"""
Trivial example to demonstrate DDT concept
"""

import argparse
import logging
import os
import time
from pathlib import Path

from src import unit_test_generator
from src.unit_test_generator import (
    generate_all_tests_and_metadata,
    unit_test_generator_decorator,
)

FMT_STR = '%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=FMT_STR)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)

# Use a global variable to test that unit_test_generator_decorator
# considers global variables when generating unit tests
error_code = 0 # pylint: disable=invalid-name

def divide_ints(a: int, b: int):
    """
    Divide two numbers, raise TypeError or ValueError if not ints 
    or denominator is 0, respectively.
    """
    global error_code # pylint: disable=global-statement
    logger.info("error_code=%d", error_code)
    if not isinstance(a, int):
        error_code = -1
        raise TypeError(f"TypeError: Variable {a=} is not an int!")
    if not isinstance(b, int):
        error_code = -2
        raise TypeError(f"TypeError: Variable {b=} is not an int!")
    if b == 0:
        error_code = -3
        raise ValueError("ValueError: Cannot divide by zero!")
    return f"{a}/{b}={a/b}"

def main():
    """
    Call division function
    """
    start = time.perf_counter()
    a_list = [6, 3,"10", 8, [], {}, 4]
    b_list = [2, 0, 2, [], 2, 3, set()]
    global error_code  # pylint: disable=global-statement
    for a, b in zip(a_list, b_list):
        try:
            logger.info("-"*80)
            error_code = 0
            try:
                logger.info("Trying divide_ints(%s, %s)", repr(a), repr(b))
            except TypeError as e:
                logger.info(e)
            print(f"divide_ints({a}, {b})={divide_ints(a, b)}")
        except (ValueError, TypeError) as e:
            logger.error("%s: %s", type(e),str(e))
        logger.info("error_code=%d", error_code)

    generate_all_tests_and_metadata(Path('.'), Path('.'))
    print(f"Took {time.perf_counter()-start} seconds")

if __name__ == "__main__":

    log_levels = {
        'critical': logging.CRITICAL,
        'error': logging.ERROR,
        'warn': logging.WARNING,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG
    }

    # Create the parser and add argument(s)
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level',
                        "-l",
                        help='log level',
                        type=str,
                        choices=log_levels.keys(),
                        default='info')
    parser.add_argument("--disable-unit-test-generation", "-d",
                        action="store_true",
                        help="Set this flag to deactivate unit test generation for this code")
    args = parser.parse_args()
    print(f"{args=}")

    this_file = Path(__file__).absolute()
    for file in this_file.parent.rglob("*"):
        if file.suffix in (".py", ".json") and file.absolute() != this_file:
            logger.debug("Deleting %s to ensure clean start", this_file)
            os.remove(file)

    # The code below applies the CLI arg above to selectively enable/disable
    # automatic unit test generation (Could not use the syntactic sugar method
    # of applying decorators as the user's input isn't parsed until now.)
    # Alternatively, move the argument parsing to the very top of this file.
    # NOTE:
    # Decorating all functions programmatically is left as an exercise to the reader:
    # Hint: https://stackoverflow.com/questions/3467526/
    divide_ints = unit_test_generator_decorator(percent_coverage=110)(divide_ints)

    main()
