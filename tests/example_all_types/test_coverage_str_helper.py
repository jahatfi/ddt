"""
Programmatically generated test function for coverage_str_helper
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 75.76% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1448', '1459', '1470', '1484-1485', '1488-1489']
@pytest.mark.parametrize(
    "this_list,non_code_lines, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            [1066, 1075, 1094, 1096, 1097, 1098, 1100, 1101, 1102],
            {1067, 1068, 1069, 1070, 1071, 1072, 1073, 1103, 1077, 1085, 1086, 1087},
            "N/A",
            "N/A",
            "N/A",
            "['1066', '1075', '1094', '1096-1098', '1100-1102']",
            "list",
            {},
            {},
        ),
    ],
)
def test_coverage_str_helper(
    this_list,
    non_code_lines,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for coverage_str_helper
    """
    x = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    if result in ["None", "True", "False"]:
        assert x is result
    else:
        assert x == result or repr(x) == result or x == repr(result)
