"""
Programmatically generated test function for add_to_my_set_kwargs()
"""

import pytest
import pass_by_assignment


# In sum, these tests covered 66.67% of add_to_my_set_kwargs's lines
# Line(s) not covered by ANY of the tests below:
# set()
@pytest.mark.parametrize(
    "kwargs, expected_result, kwargs_after",
    [
        ({"my_set": {0, 1, 2, 3}}, "None", {"my_set": {0, 1, 2, 3, 5}}),
    ],
)
def test_add_to_my_set_kwargs(kwargs, expected_result, kwargs_after):
    """
    Programmatically generated test function for add_to_my_set_kwargs()
    """
    result = pass_by_assignment.add_to_my_set_kwargs(**kwargs)
    assert result == expected_result or result == eval(expected_result)
    assert kwargs["my_set"] == kwargs_after["my_set"]
