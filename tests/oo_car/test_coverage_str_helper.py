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
from logging import Manager
from logging import StreamHandler
from logging import PlaceHolder


# In sum, these tests covered 53.12% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1759', '1766-1768', '1770', '1772-1773', '1780-1782', '1784-1785', '1788-1789']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [52, 54],
            set(),
            "['52']",
            {"this_list": "[52, 54]", "non_code_lines": "set()"},
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
