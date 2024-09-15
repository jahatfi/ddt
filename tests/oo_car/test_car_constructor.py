"""
Programmatically generated test function for Car.__init__()
"""

import re
import pytest
from collections import OrderedDict
import car


# In sum, these tests covered 100.0% of Car.__init__'s lines
@pytest.mark.parametrize(
    "color, speed, steer_angle, expected_result, args_after",
    [
        ("Red", 10, 0, "None", {"color": '"Red"', "speed": "10", "steer_angle": "0"}),
    ],
)
def test_car___init__(color, speed, steer_angle, expected_result, args_after):
    """
    Programmatically generated test function for Car.__init__()
    """
    result = car.Car(color, speed, steer_angle)
    assert isinstance(result, car.Car)
    assert result.color == color
    assert result.speed == speed
    assert result.steer_angle == steer_angle
