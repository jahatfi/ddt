"""
Programmatically generated test function for normalize_arg()
"""

import pytest
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1553', '1555', '1558-1559']
@pytest.mark.parametrize(
    "arg, expected_result, expected_type",
    [
        (
            "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
            "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
            str,
        ),
    ],
)
def test_normalize_arg(arg, expected_result, expected_type):
    """
    Programmatically generated test function for normalize_arg()
    """
    result = unit_test_generator.normalize_arg(arg)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
