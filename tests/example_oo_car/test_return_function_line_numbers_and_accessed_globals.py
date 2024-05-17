"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
from car import Car


# In sum, these tests covered 59.26% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1062', '1071', '1088-1090', '1092-1094', '1096-1098']
def test_return_function_line_numbers_and_accessed_globals_0():
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """
    # Coverage: 59.26% of function lines [1062-1100]
    # Covered Lines: 1070;1072;1074-1080;1084-1087;1091;1095;1100
    # Lines not covered: 1062-1069;1071;1088-1090;1092-1094;1096-1099
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(Car.__init__)
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(*args)
    assert x == [[33, 41, 42, 43], set(), set()]
