"""
Programmatically generated test function for Car.__init__
"""

import pytest
import car


# In sum, these tests covered 75.0% of Car.__init__'s lines
# Line(s) not covered by ANY of the tests below:
# [33]
@pytest.mark.parametrize(
    "color, speed, steer_angle, result, return_type",
    [
        ("Red", 10, 0, "None", "N/A"),
    ],
)
def test_car___init__(color, speed, steer_angle, result, return_type):
    """
    Programmatically generated test function for Car.__init__
    """
    x = car.Car(color, speed, steer_angle)
    assert isinstance(x, car.Car)
    assert x.color == color
    assert x.speed == speed
    assert x.steer_angle == steer_angle
