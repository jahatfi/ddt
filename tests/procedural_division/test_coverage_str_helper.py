"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import Logger


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1671-1672', '1675-1676', '1678', '1646', '1657', '1662-1663']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1604, 1605, 1587, 1588, 1590, 1591, 1592],
            {1600, 1601, 1593, 1595, 1596, 1597, 1598, 1599},
            "['1604-1605', '1587-1588', '1590-1592']",
            {
                "this_list": "[1604, 1605, 1587, 1588, 1590, 1591, 1592]",
                "non_code_lines": "{1600, 1601, 1593, 1595, 1596, 1597, 1598, 1599}",
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
