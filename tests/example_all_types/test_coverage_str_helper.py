"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 75.76% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1448', '1459', '1470', '1484-1485', '1488-1489']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type",
    [
        (
            [1092, 1101, 1118, 1120, 1121, 1122, 1124, 1125, 1126],
            {1093, 1094, 1095, 1096, 1097, 1098, 1099, 1127, 1103},
            "['1092', '1101', '1118', '1120-1122', '1124-1126']",
            list,
        ),
    ],
)
def test_coverage_str_helper(this_list, non_code_lines, expected_result, expected_type):
    """
    Programmatically generated test function for coverage_str_helper()
    """
    result = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
