"""
Programmatically generated test function for Car.__init__()
"""

import pytest
from tests.example_oo_car import car


# In sum, these tests covered 100.0% of Car.__init__'s lines
@pytest.mark.parametrize(
    "color, speed, steer_angle, expected_result, expected_type",
    [
        ("Red", 10, 0, "None", "N/A"),
    ],
)
def test_car___init__(color, speed, steer_angle, expected_result, expected_type):
    """
    Programmatically generated test function for Car.__init__()
    """
    result = car.Car(color, speed, steer_angle)
    assert isinstance(result, car.Car)
    assert result.color == color
    assert result.speed == speed
    assert result.steer_angle == steer_angle
