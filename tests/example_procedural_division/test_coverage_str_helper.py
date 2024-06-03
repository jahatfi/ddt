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
            [1412, 1413, 1386, 1395, 1396, 1398, 1399],
            {
                1408,
                1409,
                1387,
                1388,
                1389,
                1390,
                1391,
                1392,
                1393,
                1400,
                1402,
                1403,
                1404,
                1405,
                1406,
                1407,
            },
            "['1412-1413', '1386', '1395-1396', '1398-1399']",
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
