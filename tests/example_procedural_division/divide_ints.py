from src import unit_test_generator
from src.unit_test_generator import unit_test_generator_decorator,\
                                generate_all_tests_and_metadata
from pathlib import Path
import logging
import time
fmt_str = '%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s'
logging.basicConfig(level=logging.INFO, format=fmt_str)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)

# Use a global variable to test that unit_test_generator_decorator
# considers global variables when generating unit tests
error_code = 0

@unit_test_generator_decorator
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
    main()