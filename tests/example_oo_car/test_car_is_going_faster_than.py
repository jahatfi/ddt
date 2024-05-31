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
    "test_class_instance, other_car, result, return_type",
    [
        (Car("Red", 20, 0), Car("White", 19, 0), "True", bool),
    ],
)
def test_car_is_going_faster_than(test_class_instance, other_car, result, return_type):
    """
    Programmatically generated test function for Car.is_going_faster_than
    """
    x = test_class_instance.is_going_faster_than(other_car)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
