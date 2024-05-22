"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
from car import Car


# In sum, these tests covered 59.26% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1065', '1074', '1091-1093', '1095-1097', '1099-1101']
def test_return_function_line_numbers_and_accessed_globals_0():
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """

    # Coverage: 59.26% of function lines [1065-1103]
    # Covered Lines: 1073;1075;1077-1083;1087-1090;1094;1098;1103
    # Lines not covered: 1065-1072;1074;1091-1093;1095-1097;1099-1102
    # Note: Any lines not mentioned are comments or whitespace
    arg = Car.__init__
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(arg)
    assert x == [[33, 41, 42, 43], set(), set()]
