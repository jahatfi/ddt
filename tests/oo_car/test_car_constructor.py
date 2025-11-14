"""
Programmatically generated test function for Car.__init__()
"""

import pytest
from tests.oo_car import car


# In sum, these tests covered 100.0% of Car.__init__'s lines
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "color, speed, steer_angle, expected_result",
    [
        ("Red", 10, 0, "None"),
    ],
    ids=counter,
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
