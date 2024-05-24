"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import all_types


# In sum, these tests covered 66.67% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1066', '1075', '1094', '1096-1098', '1100-1102']
@pytest.mark.parametrize(
    "f, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            all_types.get_item_at_index,
            "N/A",
            "N/A",
            "N/A",
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
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
