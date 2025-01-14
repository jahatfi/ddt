"""
Programmatically generated test function for append_list()
"""

import re
import pytest
from collections import OrderedDict
from tests.pass_by_assignment import pass_by_assignment

# Now import modules specific to append_list:
from logging import Logger
from logging import Manager
from logging import PlaceHolder
from logging import RootLogger
from logging import StreamHandler


# In sum, these tests covered 100.0% of append_list's lines
@pytest.mark.parametrize(
    "this_list, item, expected_result, args_after",
    [
        ([1, 2, 3, 4], 6, "None", {"this_list": "[1, 2, 3, 4, 6]"}),
    ],
)
def test_append_list(this_list, item, expected_result, args_after):
    """
    Programmatically generated test function for append_list()
    """
    result = pass_by_assignment.append_list(this_list, item)
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_list == eval(args_after["this_list"])
        or args_after["this_list"] == this_list
    )
