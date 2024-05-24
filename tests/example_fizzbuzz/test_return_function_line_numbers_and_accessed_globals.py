"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import fizzbuzz


# In sum, these tests covered 70.37% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1066', '1075', '1096-1098', '1100-1102']
@pytest.mark.parametrize(
    "f, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            fizzbuzz.fizzbuzz,
            "N/A",
            "N/A",
            "N/A",
            "[[23, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57], {'mode'}, set()]",
            "list",
            {},
            {},
        ),
    ],
)
def test_return_function_line_numbers_and_accessed_globals(
    f,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(f)
    assert x == result
