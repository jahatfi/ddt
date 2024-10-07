"""
Programmatically generated test function for Car.change_steer_angle()
"""

import re
import pytest
from collections import OrderedDict
import car

# Now import modules specific to Car.change_steer_angle:
from car import Car
from logging import Manager
from logging import PlaceHolder
from logging import Logger
from logging import RootLogger
from logging import StreamHandler


# In sum, these tests covered 60.0% of Car.change_steer_angle's lines
# Line(s) not covered by ANY of the tests below:
# ['87-88']
@pytest.mark.parametrize(
    "test_class_instance, angle, exception_type, exception_message, expected_result, args_after",
    [
        (Car("Blue", 0.0, 30), 180, "N/A", "N/A", "210", {"angle": "180"}),
        (Car("White", 20, -30), 90, "N/A", "N/A", "60", {"angle": "90"}),
        (
            Car("Green", 48, 90),
            -1080,
            AssertionError,
            "angle=-1080    out of bounds!",
            "None",
            {"angle": "-1080"},
        ),
        (Car("Red", 9, 0), 30, "N/A", "N/A", "30", {"angle": "30"}),
    ],
)
def test_car_change_steer_angle(
    test_class_instance,
    angle,
    exception_type,
    exception_message,
    expected_result,
    args_after,
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
        assert angle == eval(args_after["angle"]) or args_after["angle"] == angle
