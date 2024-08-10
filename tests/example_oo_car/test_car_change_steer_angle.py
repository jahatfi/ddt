"""
Programmatically generated test function for Car.change_steer_angle()
"""

import re
import pytest

# Now import modules specific to Car.change_steer_angle:
from tests.example_oo_car.car import Car


# In sum, these tests covered 60.0% of Car.change_steer_angle's lines
# Line(s) not covered by ANY of the tests below:
# ['87-88']
@pytest.mark.parametrize(
    "test_class_instance, angle, exception_type, exception_message, expected_result",
    [
        (Car("Blue", 0.0, 30), 180, "N/A", "N/A", "210"),
        (Car("White", 20, -30), 90, "N/A", "N/A", "60"),
        (
            Car("Green", 48, 90),
            -1080,
            AssertionError,
            "angle=-1080    out of bounds!",
            "None",
        ),
        (Car("Red", 9, 0), 30, "N/A", "N/A", "30"),
    ],
)
def test_car_change_steer_angle(
    test_class_instance, angle, exception_type, exception_message, expected_result
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
