"""
Trivial example to demonstrate DDT concept
"""

import argparse
import logging
import os
import sys
import time
from pathlib import Path

import coverage

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

def divide_ints(a: int, b: int)->str:
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
