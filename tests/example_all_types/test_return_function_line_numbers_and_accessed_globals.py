"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import all_types


# In sum, these tests covered 67.86% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1092', '1101', '1118', '1120-1122', '1124-1126']
@pytest.mark.parametrize(
    "f, expected_result, expected_type",
    [
        (
            all_types.get_item_at_index,
            "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            list,
        ),
    ],
)
def test_return_function_line_numbers_and_accessed_globals(
    f, expected_result, expected_type
):
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals()
    """
    result = unit_test_generator.return_function_line_numbers_and_accessed_globals(f)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
