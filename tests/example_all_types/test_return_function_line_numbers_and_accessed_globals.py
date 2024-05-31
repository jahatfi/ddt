"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import all_types


# In sum, these tests covered 66.67% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1074', '1083', '1102', '1104-1106', '1108-1110']
@pytest.mark.parametrize(
    "f, result, return_type",
    [
        (
            all_types.get_item_at_index,
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
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
