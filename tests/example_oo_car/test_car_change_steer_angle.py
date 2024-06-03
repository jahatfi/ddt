"""
Programmatically generated test function for Car.change_steer_angle()
"""

import re
import pytest

# Now import modules specific to Car.change_steer_angle:
from tests.example_oo_car.car import Car


# In sum, these tests covered 54.55% of Car.change_steer_angle's lines
# Line(s) not covered by ANY of the tests below:
# ['71', '85-86']
@pytest.mark.parametrize(
    "test_class_instance, angle, exception_type, exception_message, expected_result, expected_type",
    [
        (
            Car("Green", 48, 90),
            -1080,
            AssertionError,
            "angle=-1080    out of bounds!",
            "None",
            "N/A",
        ),
        (Car("Red", 9, 0), 30, "N/A", "N/A", "30", int),
    ],
)
def test_car_change_steer_angle(
    test_class_instance,
    angle,
    exception_type,
    exception_message,
    expected_result,
    expected_type,
):
    """
    Programmatically generated test function for Car.change_steer_angle()
    """
    if exception_type != "N/A":
        with pytest.raises(exception_type, match=re.escape(exception_message)):
            test_class_instance.change_steer_angle(angle)
    else:
        result = test_class_instance.change_steer_angle(angle)
        assert result == expected_result or result == eval(expected_result)
