"""
Programmatically generated test function for Car.__init__
"""

import pytest
import car


# In sum, these tests covered 75.0% of Car.__init__'s lines
# Line(s) not covered by ANY of the tests below:
# [33]
@pytest.mark.parametrize(
    "self,color,speed,steer_angle, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        ("Red", 10, 0, "N/A", "N/A", "N/A", "None", "N/A", {}, {}),
    ],
)
def test_car___init__(
    self,
    color,
    speed,
    steer_angle,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for Car.__init__
    """
    x = car.Car(self, color, speed, steer_angle)
    assert isinstance(x, car.Car)
