"""
Programmatically generated test function for normalize_arg()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1728', '1730', '1733-1734']
@pytest.mark.parametrize(
    "arg, expected_result, args_after",
    [
        (
            "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, testable=0.0)",
            "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, testable=0.0)",
            {
                "arg": "\"CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, testable=0.0)\""
            },
        ),
    ],
)
def test_normalize_arg(arg, expected_result, args_after):
    """
    Programmatically generated test function for normalize_arg()
    """
    result = unit_test_generator.normalize_arg(arg)
    assert result == expected_result or result == eval(expected_result)
    assert arg == eval(args_after["arg"]) or args_after["arg"] == arg
