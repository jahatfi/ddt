"""
Programmatically generated test function for get_item_at_index
"""

import re
import pytest
from tests.example_all_types import all_types


# In sum, these tests covered 75.0% of get_item_at_index's lines
# Line(s) not covered by ANY of the tests below:
# ['22']
@pytest.mark.parametrize(
    "iterable, index, exception_type, exception_message, result, return_type",
    [
        (
            "a test string",
            -5,
            ValueError,
            "index must be in range [0, 12], was -5",
            "None",
            "N/A",
        ),
        (
            (5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
            50,
            ValueError,
            "index must be in range [0, 9], was 50",
            "None",
            "N/A",
        ),
        ([-1, -2, -3, -4], 0, "N/A", "N/A", "-1", int),
    ],
)
def test_get_item_at_index(
    iterable, index, exception_type, exception_message, result, return_type
):
    """
    Programmatically generated test function for get_item_at_index
    """
    if exception_type != "N/A":
        with pytest.raises(exception_type, match=re.escape(exception_message)):
            all_types.get_item_at_index(iterable, index)
    else:
        x = all_types.get_item_at_index(iterable, index)
        assert (
            x == result or repr(x) == result or x == repr(result) or x == eval(result)
        )
