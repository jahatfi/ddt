"""
Programmatically generated test function for normalize_arg()
"""

import pytest
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1453', '1455', '1458-1459']
@pytest.mark.parametrize(
    "arg, expected_result, expected_type",
    [
        ("None", "None", str),
    ],
)
def test_normalize_arg(arg, expected_result, expected_type):
    """
    Programmatically generated test function for normalize_arg()
    """
    result = unit_test_generator.normalize_arg(arg)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
