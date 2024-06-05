"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1479', '1490', '1495-1496', '1504-1505', '1508-1509']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type",
    [
        (
            [1420, 1421, 1423, 1424, 1437, 1438],
            {1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434},
            "['1420-1421', '1423-1424', '1437-1438']",
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
