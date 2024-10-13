"""
Test case to demonstrate the DDT concept on a variant of the fizzbuzz problem.
Includes a global variable.
"""
import argparse
import logging
import os
from pathlib import Path
import coverage
import json

from src import unit_test_generator
from src.unit_test_generator import (
    generate_all_tests_and_metadata,
    unit_test_generator_decorator,
    Capturing
)

FMT_STR = '%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=FMT_STR)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.WARNING)

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

def main():
    """
    Begin ad hoc tests
    """
    global mode # pylint: disable=global-statement
    cov = coverage.Coverage()
    with cov.collect():
        print(fizzbuzz(6))
        print(fizzbuzz(30))
        mode = 'buzzfizz'
        print(fizzbuzz(6))
        print(fizzbuzz(30))
        mode = "a_test"
        print(fizzbuzz(6))
    cov.save()
    '''
    with Capturing() as stdout_lines:
        cov.json_report(outfile='-')
    # result will not exist if the function threw an exception
    cov_report_ = json.loads(stdout_lines[0])
    logger.critical(cov_report_)
    '''
    
    # The generate_all_tests_and_metadata() function takes 2 Paths:
    # 1. The output directory for the unit tests (.py)
    # 2. The output directory for the .json files (I/O for each test)

    generate_all_tests_and_metadata(Path('.'), Path('.'))

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
    #fizzbuzz = unit_test_generator_decorator(not args.disable_unit_test_generation)(fizzbuzz)

    main()
