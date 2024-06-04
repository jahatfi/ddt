"""
Programmatically generated test function for normalize_arg()
"""

import pytest
from src import unit_test_generator


# In sum, these tests covered 54.55% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1422', '1431', '1433', '1436-1437']
@pytest.mark.parametrize(
    "arg, expected_result, expected_type",
    [
        (
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
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
