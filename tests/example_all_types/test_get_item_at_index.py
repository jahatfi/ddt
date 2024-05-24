"""
Programmatically generated test function for get_item_at_index
"""

import pytest
import all_types


# In sum, these tests covered 75.0% of get_item_at_index's lines
# Line(s) not covered by ANY of the tests below:
# ['22']
@pytest.mark.parametrize(
    "iterable,index, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            "a test string",
            -5,
            "N/A",
            "<class 'ValueError'>",
            "index must be in range [0, 12], was -5",
            "None",
            "N/A",
            {},
            {},
        ),
        (
            (5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
            50,
            "N/A",
            "<class 'ValueError'>",
            "index must be in range [0, 9], was 50",
            "None",
            "N/A",
            {},
            {},
        ),
        ([-1, -2, -3, -4], 0, "N/A", "N/A", "N/A", "-1", "int", {}, {}),
    ],
)
def test_get_item_at_index(
    iterable,
    index,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for get_item_at_index
    """
    with pytest.raises(
        ValueError, match=r"index\ must\ be\ in\ range\ \[0,\ 12\],\ was\ \-5"
    ):
        all_types.get_item_at_index(iterable, index)
