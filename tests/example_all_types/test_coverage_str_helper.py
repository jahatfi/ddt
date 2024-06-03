"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 75.76% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1443', '1454', '1465', '1479-1480', '1483-1484']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type",
    [
        (
            [1087, 1096, 1113, 1115, 1116, 1117, 1119, 1120, 1121],
            {1088, 1089, 1090, 1091, 1092, 1093, 1094, 1122, 1098},
            "['1087', '1096', '1113', '1115-1117', '1119-1121']",
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
