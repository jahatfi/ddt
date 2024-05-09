"""
Programmatically generated test function for return_function_line_numbers_and_accessed_globals
"""

from src import unit_test_generator

# Now import modules specific to return_function_line_numbers_and_accessed_globals:
import divide_ints


# In sum, these tests covered 81.48% of return_function_line_numbers_and_accessed_globals's lines
# Line(s) not covered by ANY of the tests below:
# ['1068', '1077', '1102-1104']
def test_return_function_line_numbers_and_accessed_globals_0():
    """
    Programmatically generated test function for return_function_line_numbers_and_accessed_globals
    """
    # Coverage: 81.48% of function lines [1068-1106]
    # Covered Lines: 1076;1078;1080-1086;1090-1101;1106
    # Lines not covered: 1068-1075;1077;1102-1105
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(divide_ints.divide_ints)
    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(*args)
    assert x == [
        [26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        {"error_code", "logger"},
        {"error_code"},
    ]
