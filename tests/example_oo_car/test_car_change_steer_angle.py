"""
Programmatically generated test function for Car.change_steer_angle
"""

import pytest

# Now import modules specific to Car.change_steer_angle:
from tests.example_oo_car.car import Car


# In sum, these tests covered 54.55% of Car.change_steer_angle's lines
# Line(s) not covered by ANY of the tests below:
# ['71', '85-86']
def test_car_change_steer_angle_0():
    """
    Programmatically generated test function for Car.change_steer_angle
    """
    # Coverage: 27.27% of function lines [71-88]
    # Covered Lines: 77-79
    # Lines not covered: 71-76;81-88
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(-1080)
    this_class = Car("Green", 48, 90)
    with pytest.raises(AssertionError, match=r"angle=\-1080\ \ \ \ out\ of\ bounds!"):
        this_class.change_steer_angle(*args)


def test_car_change_steer_angle_1():
    """
    Programmatically generated test function for Car.change_steer_angle
    """
    # Coverage: 45.45% of function lines [71-88]
    # Covered Lines: 77-78;81;84;88
    # Lines not covered: 71-76;79-80;85-87
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(30)
    this_class = Car("Red", 9, 0)
    x = this_class.change_steer_angle(*args)
    assert x == 30
