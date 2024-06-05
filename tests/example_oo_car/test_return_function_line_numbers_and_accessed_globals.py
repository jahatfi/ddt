"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
from car import Car


# In sum, these tests covered 59.26% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1071', '1080', '1097-1099', '1101-1103', '1105-1107']
def test_return_function_line_numbers_and_accessed_globals_0():
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """

    # Coverage: 59.26% of function lines [1071-1109]
    # Covered Lines: 1079;1081;1083-1089;1093-1096;1100;1104;1109
    # Lines not covered: 1071-1078;1080;1097-1099;1101-1103;1105-1108
    # Note: Any lines not mentioned are comments or whitespace
    arg = Car.__init__
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(arg)
    assert x == [[33, 41, 42, 43], set(), set()]
