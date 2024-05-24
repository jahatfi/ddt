"""
Programmatically generated test function for Car.change_steer_angle
"""

import pytest

# Now import modules specific to Car.change_steer_angle:
from car import Car


# In sum, these tests covered 54.55% of Car.change_steer_angle's lines
# Line(s) not covered by ANY of the tests below:
# ['71', '85-86']
@pytest.mark.parametrize(
    "self,angle, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            -1080,
            "N/A",
            "<class 'AssertionError'>",
            "angle=-1080    out of bounds!",
            "None",
            "N/A",
            {},
            {},
        ),
        (30, "N/A", "N/A", "N/A", "30", "int", {}, {}),
    ],
)
def test_car_change_steer_angle(
    self,
    angle,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for Car.change_steer_angle
    """
    this_class = Car("Green", 48, 90)
    arg = -1080
    with pytest.raises(AssertionError, match=r"angle=\-1080\ \ \ \ out\ of\ bounds!"):
        this_class.change_steer_angle(self)
