"""
Programmatically generated test function for increment_my_list_kwargs()
"""

import pytest
import pass_by_assignment


# In sum, these tests covered 66.67% of increment_my_list_kwargs's lines
# Line(s) not covered by ANY of the tests below:
# set()
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "kwargs, expected_result, kwargs_after",
    [
        ({"my_list": [0, 3]}, "None", {"my_list": [0, 3, 1]}),
    ],
    ids=counter,
)
def test_increment_my_list_kwargs(kwargs, expected_result, kwargs_after):
    """
    Programmatically generated test function for increment_my_list_kwargs()
    """
    result = pass_by_assignment.increment_my_list_kwargs(**kwargs)
    assert result == expected_result or result == eval(expected_result)
    kwargs["my_list"] == kwargs_after["my_list"]
