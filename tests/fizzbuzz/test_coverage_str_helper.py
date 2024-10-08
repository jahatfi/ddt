"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import RootLogger
from logging import Logger
from logging import StreamHandler
from logging import Manager
from logging import PlaceHolder


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1759', '1770', '1775-1776', '1784-1785', '1788-1789']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1699, 1700, 1702, 1703, 1704, 1716, 1717],
            {1705, 1707, 1708, 1709, 1710, 1711, 1712, 1713},
            "['1699-1700', '1702-1704', '1716-1717']",
            {
                "this_list": "[1699, 1700, 1702, 1703, 1704, 1716, 1717]",
                "non_code_lines": "{1705, 1707, 1708, 1709, 1710, 1711, 1712, 1713}",
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
