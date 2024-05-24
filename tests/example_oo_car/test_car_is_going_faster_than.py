"""
Programmatically generated test function for Car.is_going_faster_than
"""

import pytest

# Now import modules specific to Car.is_going_faster_than:
from car import Car


# In sum, these tests covered 50.0% of Car.is_going_faster_than's lines
# Line(s) not covered by ANY of the tests below:
# [117]
@pytest.mark.parametrize(
    "self,other_car, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (Car("White", 19, 0), "N/A", "N/A", "N/A", "True", "bool", {}, {}),
    ],
)
def test_car_is_going_faster_than(
    self,
    other_car,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for Car.is_going_faster_than
    """
    this_class = Car("Red", 20, 0)
    arg = Car("White", 19, 0)
    x = this_class.is_going_faster_than(self)
    assert x is True
