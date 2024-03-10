from src import unit_test_generator
from src.unit_test_generator import unit_test_generator_decorator,\
                                generate_all_tests_and_metadata
from pathlib import Path
import logging
import argparse
import time
fmt_str = '%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=fmt_str)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)

# Use a global variable to test that unit_test_generator_decorator
# considers global variables when generating unit tests
error_code = 0

def divide_ints(a: int, b: int):
    global error_code    
    logger.info(f"{error_code=}")
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
    start = time.perf_counter()
    a_list = [6, 3,"10", 8, [], {}, 4]
    b_list = [2, 0, 2, [], 2, 3, set()]

    for a, b in zip(a_list, b_list):
        try:
            logger.info("-"*80)
            error_code = 0
            logger.info(f"Trying divide_ints({a}, {b})")
            logger.info(f"divide_ints({a}, {b})={divide_ints(a, b)}")
        except Exception as e:
            logger.error(f"{type(e)}: {e}")
        logger.info(f"{error_code=}")

    generate_all_tests_and_metadata(Path('.'), Path('.'))
    print(f"Took {time.perf_counter()-start} seconds")

if __name__ == "__main__":
    # Create the parser and add argument(s)
    parser = argparse.ArgumentParser()
    parser.add_argument("--disable-unit-test-generation", "-d",
                        action="store_true",
                        help="Set this flag to deactivate unit test generation for this code")
    args = parser.parse_args()
    print(f"{args=}")

    # The code below applies the CLI arg above to selectively enable/disable
    # automatic unit test generation (Could not use the syntactic sugar method
    # of applying decorators as the user's input isn't parsed until now.)
    # Alternatively, move the argument parsing to the very top of this file.
    # NOTE:
    # Decorating all functions programmatically is left as an exercise to the reader:
    # Hint: https://stackoverflow.com/questions/3467526/
    divide_ints = unit_test_generator_decorator(not args.disable_unit_test_generation)(divide_ints)

    main()