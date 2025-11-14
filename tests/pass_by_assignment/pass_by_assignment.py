"""
Test case to demonstrate tests for pass by assignment.
"""

import logging
from typing import Any, List, TypeVar

from src import unit_test_generator
from src.unit_test_generator import (
    unit_test_generator_decorator,
)

T = TypeVar('T')

FMT_STR = "%(levelname)-8s|%(module)-16s|%(funcName)-20s:%(lineno)-4d:%(message)s"
logging.basicConfig(level=logging.INFO, format=FMT_STR)
logger = logging.getLogger(__name__)
unit_test_generator.logger.setLevel(logging.CRITICAL)

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
    Given a list of items; overwrite the local copy.
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

@unit_test_generator_decorator(sample_count=6, keep_subsets=True, percent_coverage=0)
def add_to_my_set_kwargs(**kwargs):
    """
    If kwargs contains an entry "my_set" that is a list,
    append a 1 to it.
    """
    if "my_set" in kwargs and isinstance(kwargs["my_set"], set):
        kwargs["my_set"].add(1)