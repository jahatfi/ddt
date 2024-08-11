"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 78.12% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1670', '1684-1685', '1688-1689', '1691']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1424, 1436, 1445, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1461, 1462],
            {1426, 1444, 1446, 1434},
            "['1424', '1436', '1445', '1448-1454', '1461-1462']",
            {
                "this_list": "[1424, 1436, 1445, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1461, 1462]",
                "non_code_lines": "{1426, 1444, 1446, 1434}",
            },
        ),
    ],
)
def test_coverage_str_helper(this_list, non_code_lines, expected_result, args_after):
    """
    Programmatically generated test function for coverage_str_helper()
    """
    result = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_list == eval(args_after["this_list"])
        or args_after["this_list"] == this_list
    )
    assert (
        non_code_lines == eval(args_after["non_code_lines"])
        or args_after["non_code_lines"] == non_code_lines
    )
