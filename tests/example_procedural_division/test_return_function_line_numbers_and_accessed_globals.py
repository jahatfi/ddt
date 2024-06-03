"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import divide_ints


# In sum, these tests covered 82.14% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1087', '1096', '1119-1121']
@pytest.mark.parametrize(
    "f, expected_result, expected_type",
    [
        (
            divide_ints.divide_ints,
            "[[26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], {'logger', 'error_code'}, {'error_code'}]",
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
