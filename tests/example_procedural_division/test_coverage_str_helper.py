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
            [1417, 1418, 1391, 1400, 1401, 1403, 1404],
            {
                1408,
                1409,
                1410,
                1411,
                1412,
                1413,
                1414,
                1392,
                1393,
                1394,
                1395,
                1396,
                1397,
                1398,
                1405,
                1407,
            },
            "['1417-1418', '1391', '1400-1401', '1403-1404']",
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
