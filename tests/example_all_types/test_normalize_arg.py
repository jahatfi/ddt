"""
Programmatically generated test function for normalize_arg
"""

import pytest
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1421', '1430', '1432']
@pytest.mark.parametrize(
    "arg, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            "N/A",
            "N/A",
            "N/A",
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            "str",
            {},
            {},
        ),
    ],
)
def test_normalize_arg(
    arg,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for normalize_arg
    """
    x = unit_test_generator.normalize_arg(arg)
    assert x == result or repr(x) == result or repr(result) == x
