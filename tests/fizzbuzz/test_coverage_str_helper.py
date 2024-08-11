"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import Manager
from logging import StreamHandler
from logging import PlaceHolder
from logging import RootLogger
from logging import Logger


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1664', '1675', '1680-1681', '1689-1690', '1693-1694']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1605, 1606, 1608, 1609, 1610, 1622, 1623],
            {1611, 1613, 1614, 1615, 1616, 1617, 1618, 1619},
            "['1605-1606', '1608-1610', '1622-1623']",
            {
                "this_list": "[1605, 1606, 1608, 1609, 1610, 1622, 1623]",
                "non_code_lines": "{1611, 1613, 1614, 1615, 1616, 1617, 1618, 1619}",
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
