"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1477', '1488', '1493-1494', '1502-1503', '1506-1507']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type",
    [
        (
            [1418, 1419, 1421, 1422, 1435, 1436],
            {1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432},
            "['1418-1419', '1421-1422', '1435-1436']",
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
