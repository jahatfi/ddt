"""
Programmatically generated test function for coverage_str_helper
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 75.76% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1464', '1475', '1486', '1500-1501', '1504-1505']
@pytest.mark.parametrize(
    "this_list, non_code_lines, result, return_type",
    [
        (
            [1074, 1083, 1102, 1104, 1105, 1106, 1108, 1109, 1110],
            {1093, 1094, 1095, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1111, 1085},
            "['1074', '1083', '1102', '1104-1106', '1108-1110']",
            list,
        ),
    ],
)
def test_coverage_str_helper(this_list, non_code_lines, result, return_type):
    """
    Programmatically generated test function for coverage_str_helper
    """
    x = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
