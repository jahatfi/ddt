"""
Programmatically generated test function for normalize_arg()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1721', '1723', '1726-1727']
@pytest.mark.parametrize(
    "arg, expected_result",
    [
        (
            "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, testable=0.0)",
            "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, testable=0.0)",
        ),
    ],
)
def test_normalize_arg(arg, expected_result):
    """
    Programmatically generated test function for normalize_arg()
    """
    result = unit_test_generator.normalize_arg(arg)
    assert result == expected_result or result == eval(expected_result)
