"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import PlaceHolder
from logging import RootLogger
from logging import Manager
from logging import StreamHandler
from logging import Logger


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1681', '1692', '1697-1698', '1706-1707', '1710-1711']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1638, 1639, 1621, 1622, 1624, 1625, 1626],
            {1632, 1633, 1634, 1635, 1627, 1629, 1630, 1631},
            "['1638-1639', '1621-1622', '1624-1626']",
            {
                "this_list": "[1638, 1639, 1621, 1622, 1624, 1625, 1626]",
                "non_code_lines": "{1632, 1633, 1634, 1635, 1627, 1629, 1630, 1631}",
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
