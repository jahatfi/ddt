"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import fizzbuzz


# In sum, these tests covered 71.43% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1087', '1096', '1115-1117', '1119-1121']
@pytest.mark.parametrize(
    "f, expected_result, expected_type",
    [
        (
            fizzbuzz.fizzbuzz,
            "[[23, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57], {'mode'}, set()]",
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
