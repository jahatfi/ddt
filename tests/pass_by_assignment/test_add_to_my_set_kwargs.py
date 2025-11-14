"""
Programmatically generated test function for add_to_my_set_kwargs()
"""

import pytest
from tests.pass_by_assignment import pass_by_assignment


# In sum, these tests covered 66.67% of add_to_my_set_kwargs's lines
# Line(s) not covered by ANY of the tests below:
# set()
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "kwargs, expected_result, kwargs_after",
    [
        ({"my_set": {0, 2, 3}}, "None", {"my_set": {0, 1, 2, 3}}),
    ],
    ids=counter,
)
def test_add_to_my_set_kwargs(kwargs, expected_result, kwargs_after):
    """
    Programmatically generated test function for add_to_my_set_kwargs()
    """
    result = pass_by_assignment.add_to_my_set_kwargs(**kwargs)
    assert result == expected_result or result == eval(expected_result)
    kwargs["my_set"] == kwargs_after["my_set"]
