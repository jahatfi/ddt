"""
Programmatically generated test function for normalize_arg
"""

import pytest
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1448', '1450', '1453']
@pytest.mark.parametrize(
    "arg, result, return_type",
    [
        (
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            str,
        ),
    ],
)
def test_normalize_arg(arg, result, return_type):
    """
    Programmatically generated test function for normalize_arg
    """
    x = unit_test_generator.normalize_arg(arg)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
