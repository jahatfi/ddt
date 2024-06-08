"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 68.75% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1481', '1492', '1502-1504', '1506-1507', '1510-1511']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type",
    [
        (
            [1440, 1422, 1423, 1425, 1426, 1427, 1439],
            {1428, 1430, 1431, 1432, 1433, 1434, 1435, 1436},
            "['1440', '1422-1423', '1425-1427']",
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
