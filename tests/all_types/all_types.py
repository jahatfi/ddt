"""
Test case to demonstrate various Python types such as lists, dictionaries, etc.
"""

import argparse
import logging
import os
from pathlib import Path

import coverage

from src import unit_test_generator
from src.unit_test_generator import (
    generate_all_tests_and_metadata,
    unit_test_generator_decorator,
)

FMT_STR = "%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s"
logging.basicConfig(level=logging.INFO, format=FMT_STR)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)


@unit_test_generator_decorator(sample_count=6, keep_subsets=True, percent_coverage=0)
def get_item_at_index(iterable, index: int):
    """
    Used to test unit_test_generator_decorator with
    string, tuple, list, and int arguments.

    """
    if not iterable:
        raise ValueError("iterable cannot be empty!")
    if index >= len(iterable):
        raise ValueError(f"index must be in range [0, {len(iterable)-1}], was {index}")
    if index < 0:
        raise ValueError(f"index must be in range [0, {len(iterable)-1}], was {index}")

    return iterable[index]


# @unit_test_generator_decorator(sample_count=4)
def get_key_to_set_with_highest_value(dictionary: dict):
    """
    Used to test unit_test_generator_decorator with
    dictionary and set arguments.

    Given a dictionary mapping arbitary numeric keys to
    sets of numbers, return the key to the set with the
    overall highest value.  In case of ties, return the
    lowest key.
    """
    # Sort the keys so lowest key is kept in case of ties
    # The linear search will therefore use '>', not '>=
    keys = sorted(list(dictionary.keys()))
    # Take the first key, max(set) pair as the initial best value
    best_key = keys[0]
    highest_value = max(dictionary[keys[0]])
    # Now conduct linear search over the rest of the dictionary
    # Skip the first key since we started with that one
    for this_key in keys[1:]:
        this_highest_value = max(dictionary[this_key])
        if this_highest_value > highest_value:
            best_key = this_key
            highest_value = this_highest_value
    return best_key


def main():
    """
    Execute the functions above.
    """
    # Begin ad hoc tests
    # Test get_item_at_index
    iterables = [
        "The quick red fox jumped over the lazy brown dog",
        tuple(list(range(5, 15))), # pylint: disable=consider-using-generator
        [-1, -2, -3, -4],
        "a test string",
        "a test string",
        # set([])
    ]
    indices = [3, 50, 0, -5, -5]
    for iterable, index in zip(iterables, indices):
        logger.info("index=%d iterable=%s", index, iterable)
        try:
            print(f"{get_item_at_index(iterable, index)=}")
        except ValueError as e:
            logger.error(e)

    my_dict = {
        10: set([90, 95, 100]),
        3: set([20, 40, 80]),
        -1: set([x * x for x in range(10)]), # pylint: disable=consider-using-set-comprehension
    }
    print(f"{get_key_to_set_with_highest_value(my_dict)=}")


    # The generate_all_tests_and_metadata() function takes 2 Paths:
    # 1. The output directory for the unit tests (.py)
    # 2. The output directory for the .json files (I/O for each test)

    generate_all_tests_and_metadata(Path("."), Path("."))


if __name__ == "__main__":
    log_levels = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warn": logging.WARNING,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
    }
    # Create the parser and add argument(s)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--log-level",
        "-l",
        help="log level",
        type=str,
        choices=log_levels.keys(),
        default="info",
    )
    parser.add_argument(
        "--disable-unit-test-generation",
        "-d",
        action="store_true",
        help="Set this flag to deactivate unit test generation for this code",
    )
    args = parser.parse_args()
    logger.setLevel(log_levels[args.log_level])
    logger.info("args=%s", args)

    this_file = Path(__file__).absolute()
    for file in this_file.parent.rglob("*"):
        if file.suffix in (".py", ".json") and file.absolute() != this_file:
            logger.debug("Deleting %s to ensure clean start", this_file)
            os.remove(file)

    logger.info("%s", __file__)
    # The code below applies the CLI arg above to selectively enable/disable
    # automatic unit test generation (Could not use the syntactic sugar method
    # of applying decorators as the user's input isn't parsed until now.)
    # Alternatively, move the argument parsing to the very top of this file.
    # NOTE:
    # Decorating all functions programmatically is left as an exercise to the reader:
    # Hint: https://stackoverflow.com/questions/3467526/
    # get_key_to_set_with_highest_value = unit_test_generator_decorator(not args.disable_unit_test_generation)(get_key_to_set_with_highest_value) # pylint: disable=line-too-long
    # get_item_at_index = unit_test_generator_decorator(not args.disable_unit_test_generation)(get_item_at_index) # pylint: disable=line-too-long

    cov = coverage.Coverage()
    with cov.collect():
        main()
    cov.save()
