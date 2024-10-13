"""
Programmatically generated test function for get_item_at_index()
"""

import re
import pytest
from collections import OrderedDict
import all_types


# In sum, these tests covered 85.71% of get_item_at_index's lines
# Line(s) not covered by ANY of the tests below:
# [30]
@pytest.mark.parametrize(
    "iterable, index, exception_type, exception_message, expected_result, args_after",
    [
        ("The quick red fox jumped over the lazy brown dog", 3, "N/A", "N/A", " ", {}),
        (
            "a test string",
            -5,
            ValueError,
            "index must be in range [0, 12], was -5",
            "None",
            {},
        ),
        (
            (5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
            50,
            ValueError,
            "index must be in range [0, 9], was 50",
            "None",
            {"iterable": "(5, 6, 7, 8, 9, 10, 11, 12, 13, 14)"},
        ),
        ([-1, -2, -3, -4], 0, "N/A", "N/A", "-1", {"iterable": "[-1, -2, -3, -4]"}),
    ],
)
def test_get_item_at_index(
    iterable, index, exception_type, exception_message, expected_result, args_after
):
    """
    Programmatically generated test function for get_item_at_index()
    """
    if exception_type != "N/A":
        with pytest.raises(exception_type, match=re.escape(exception_message)):
            all_types.get_item_at_index(iterable, index)
    else:
        result = all_types.get_item_at_index(iterable, index)
        assert result == expected_result or result == eval(expected_result)
