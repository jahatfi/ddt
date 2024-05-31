"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import fizzbuzz


# In sum, these tests covered 70.37% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1074', '1083', '1104-1106', '1108-1110']
@pytest.mark.parametrize(
    "f, result, return_type",
    [
        (
            fizzbuzz.fizzbuzz,
            "[[23, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57], {'mode'}, set()]",
            list,
        ),
    ],
)
def test_return_function_line_numbers_and_accessed_globals(f, result, return_type):
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(f)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
