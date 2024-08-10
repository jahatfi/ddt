"""
Programmatically generated test function for Car.__init__()
"""

import pytest
import car


# In sum, these tests covered 100.0% of Car.__init__'s lines
@pytest.mark.parametrize(
    "color, speed, steer_angle, expected_result",
    [
        ("Red", 10, 0, "None"),
    ],
)
def test_car___init__(color, speed, steer_angle, expected_result):
    """
    Programmatically generated test function for Car.__init__()
    """
    result = car.Car(color, speed, steer_angle)
    assert isinstance(result, car.Car)
    assert result.color == color
    assert result.speed == speed
    assert result.steer_angle == steer_angle
