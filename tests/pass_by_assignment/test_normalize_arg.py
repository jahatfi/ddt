"""
Programmatically generated test function for normalize_arg()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1728', '1730', '1733-1734']
@pytest.mark.parametrize(
    "arg, expected_result, args_after",
    [
        ("None", "None", {"arg": '"None"'}),
    ],
)
def test_normalize_arg(arg, expected_result, args_after):
    """
    Programmatically generated test function for normalize_arg()
    """
    result = unit_test_generator.normalize_arg(arg)
    assert result == expected_result or result == eval(expected_result)
    assert arg == eval(args_after["arg"]) or args_after["arg"] == arg
