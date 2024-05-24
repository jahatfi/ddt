"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import divide_ints


# In sum, these tests covered 81.48% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1066', '1075', '1100-1102']
@pytest.mark.parametrize(
    "f, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            divide_ints.divide_ints,
            "N/A",
            "N/A",
            "N/A",
            "[[26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], {'error_code', 'logger'}, {'error_code'}]",
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
