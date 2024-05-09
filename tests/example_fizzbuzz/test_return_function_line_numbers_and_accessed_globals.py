"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import fizzbuzz


# In sum, these tests covered 70.37% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1068', '1077', '1098-1100', '1102-1104']
def test_return_function_line_numbers_and_accessed_globals_0():
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """
    # Coverage: 70.37% of function lines [1068-1106]
    # Covered Lines: 1076;1078;1080-1086;1090-1097;1101;1106
    # Lines not covered: 1068-1075;1077;1098-1100;1102-1105
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(fizzbuzz.fizzbuzz)
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(*args)
    assert x == [
        [23, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57],
        {"mode"},
        set(),
    ]
