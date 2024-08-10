"""
Programmatically generated test function for normalize_arg()
"""

import re
import pytest
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1618', '1620', '1623-1624']
@pytest.mark.parametrize(
    "arg, expected_result",
    [
        ("None", "None"),
    ],
)
def test_normalize_arg(arg, expected_result):
    """
    Programmatically generated test function for normalize_arg()
    """
    result = unit_test_generator.normalize_arg(arg)
    assert result == expected_result or result == eval(expected_result)
