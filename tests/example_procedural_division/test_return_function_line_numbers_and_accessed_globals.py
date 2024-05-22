"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import divide_ints


# In sum, these tests covered 81.48% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1066', '1075', '1100-1102']
def test_return_function_line_numbers_and_accessed_globals_0():
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """

    # Coverage: 81.48% of function lines [1066-1104]
    # Covered Lines: 1074;1076;1078-1084;1088-1099;1104
    # Lines not covered: 1066-1073;1075;1100-1103
    # Note: Any lines not mentioned are comments or whitespace
    arg = divide_ints.divide_ints
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(arg)
    assert x == [
        [26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        {"error_code", "logger"},
        {"error_code"},
    ]
