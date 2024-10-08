"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import Manager
from logging import StreamHandler
from logging import RootLogger
from logging import Logger
from logging import PlaceHolder


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1743', '1754', '1759-1760', '1768-1769', '1772-1773']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1701, 1702, 1684, 1685, 1687, 1688, 1689],
            {1696, 1697, 1698, 1690, 1692, 1693, 1694, 1695},
            "['1701-1702', '1684-1685', '1687-1689']",
            {
                "this_list": "[1701, 1702, 1684, 1685, 1687, 1688, 1689]",
                "non_code_lines": "{1696, 1697, 1698, 1690, 1692, 1693, 1694, 1695}",
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
