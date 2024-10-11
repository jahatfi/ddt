"""
Programmatically generated test function for overwrite_list()
"""

import re
import pytest
from collections import OrderedDict
import pass_by_assignment


# In sum, these tests covered 100.0% of overwrite_list's lines
@pytest.mark.parametrize(
    "this_list, expected_result, args_after",
    [
        ([6, 4, 3, 2, 1], "None", {"this_list": "[6, 4, 3, 2, 1]"}),
    ],
)
def test_overwrite_list(this_list, expected_result, args_after):
    """
    Programmatically generated test function for overwrite_list()
    """
    result = pass_by_assignment.overwrite_list(this_list)
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_list == eval(args_after["this_list"])
        or args_after["this_list"] == this_list
    )
