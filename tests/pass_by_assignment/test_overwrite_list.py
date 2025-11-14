"""
Programmatically generated test function for overwrite_list()
"""

import pytest
import pass_by_assignment


# In sum, these tests covered 100.0% of overwrite_list's lines
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "this_list, expected_result, args_after",
    [
        ([6, 4, 3, 2, 1], "None", {"this_list": "[6, 4, 3, 2, 1]"}),
    ],
    ids=counter,
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
