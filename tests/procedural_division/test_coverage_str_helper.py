"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import StreamHandler
from logging import Logger
from logging import PlaceHolder
from logging import RootLogger
from logging import Manager


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1757', '1768', '1773-1774', '1782-1783', '1786-1787']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1697, 1698, 1700, 1701, 1702, 1714, 1715],
            {1703, 1705, 1706, 1707, 1708, 1709, 1710, 1711},
            "['1697-1698', '1700-1702', '1714-1715']",
            {
                "this_list": "[1697, 1698, 1700, 1701, 1702, 1714, 1715]",
                "non_code_lines": "{1703, 1705, 1706, 1707, 1708, 1709, 1710, 1711}",
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
