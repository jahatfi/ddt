"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import Logger
from logging import Manager
from logging import PlaceHolder
from logging import RootLogger
from logging import StreamHandler


# In sum, these tests covered 37.5% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1750', '1756-1764', '1766-1769', '1771-1773', '1775-1776']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        ([32], {37}, "[32]", {"this_list": "[32]", "non_code_lines": "{37}"}),
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
