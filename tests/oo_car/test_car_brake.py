"""
Programmatically generated test function for Car.brake()
"""

import re
import pytest
from collections import OrderedDict
from tests.oo_car import car

# Now import modules specific to Car.brake:
from logging import Logger
from logging import PlaceHolder
from logging import StreamHandler
from logging import Manager
from logging import RootLogger
from tests.oo_car.car import Car


# In sum, these tests covered 71.43% of Car.brake's lines
# Line(s) not covered by ANY of the tests below:
# ['52']
@pytest.mark.parametrize(
    "test_class_instance, rate, duration, expected_result, args_after",
    [
        (Car("Red", 10, 0), -1, 1, "9", {"rate": "-1", "duration": "1"}),
    ],
)
def test_car_brake(test_class_instance, rate, duration, expected_result, args_after):
    """
    Programmatically generated test function for Car.brake()
    """
    result = test_class_instance.brake(rate, duration)
    assert result == expected_result or result == eval(expected_result)
    assert rate == eval(args_after["rate"]) or args_after["rate"] == rate
    assert (
        duration == eval(args_after["duration"]) or args_after["duration"] == duration
    )
