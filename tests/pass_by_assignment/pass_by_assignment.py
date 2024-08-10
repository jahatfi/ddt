"""
Test case to demonstrate tests for pass by assignment.
"""

import argparse
import logging
import os
from pathlib import Path
from typing import Any, List, TypeVar

from src import unit_test_generator
from src.unit_test_generator import (
    generate_all_tests_and_metadata,
    unit_test_generator_decorator,
)

T = TypeVar('T')


class ClassForTesting():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"ClassForTesting('{self.name}')"
    
    def __eq__(self, __value: Any) -> bool:
        return self.name == __value.name

FMT_STR = "%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s"
logging.basicConfig(level=logging.INFO, format=FMT_STR)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.DEBUG)

@unit_test_generator_decorator(sample_count=6, keep_subsets=True, percent_coverage=0)
def append_list(this_list:List[Any], item:Any)->None:
    """
    Given a list of items of the same type T and a separate item,
    append the item to the list.  Return None.
    """
    logger.info("APPEND %s to %s", item, this_list)
    this_list.append(item)
    

@unit_test_generator_decorator(sample_count=6, keep_subsets=True, percent_coverage=0)
def overwrite_list(this_list:List[Any])->None:
    """
    Given a list of items of the same type T and a separate item,
    delete the local copy.
    """
    this_list = [0]
    print(this_list)

@unit_test_generator_decorator(sample_count=6, keep_subsets=True, percent_coverage=0)
def increment_my_list_kwargs(**kwargs):
    """
    If kwargs contains an entry "my_list" that is a list,
    append a 1 to it.
    """
    if "my_list" in kwargs and isinstance(kwargs["my_list"], list):
        kwargs["my_list"].append(1)
        kwargs["my_list"].append(ClassForTesting("test"))

@unit_test_generator_decorator(sample_count=6, keep_subsets=True, percent_coverage=0)
def add_to_my_set_kwargs(**kwargs):
    """
    If kwargs contains an entry "my_set" that is a list,
    append a 1 to it.
    """
    if "my_set" in kwargs and isinstance(kwargs["my_set"], set):
        kwargs["my_set"].add(1)
        

def main():
    """
    Execute the functions above.
    """
    # Begin ad hoc tests
    # Test append_list
    
    my_list = [1,2,3,4]
    append_list(my_list, 6)
    overwrite_list(my_list[::-1])

    kwargs = {"my_list":[0,3]}
    print(f"Before: {kwargs=}")
    increment_my_list_kwargs(**kwargs)
    print(f"After: {kwargs=}")
    
    
    kwargs = {}
    kwargs["my_set"] = set([0,2,3])
    add_to_my_set_kwargs(**kwargs)
    print(f"After: {kwargs=}")
    
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

    main()
