"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import all_types


# In sum, these tests covered 66.67% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1066', '1075', '1094', '1096-1098', '1100-1102']
def test_return_function_line_numbers_and_accessed_globals_0():
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """

    # Coverage: 66.67% of function lines [1066-1104]
    # Covered Lines: 1074;1076;1078-1084;1088-1093;1095;1099;1104
    # Lines not covered: 1066-1073;1075;1094;1096-1098;1100-1103
    # Note: Any lines not mentioned are comments or whitespace
    arg = all_types.get_item_at_index
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(arg)
    assert x == [[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]
