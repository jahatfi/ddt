"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
from car import Car


# In sum, these tests covered 59.26% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1066', '1075', '1092-1094', '1096-1098', '1100-1102']
@pytest.mark.parametrize(
    "f, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            Car.__init__,
            "N/A",
            "N/A",
            "N/A",
            "[[33, 41, 42, 43], set(), set()]",
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
    assert x == result or repr(x) == result or repr(result) == x
