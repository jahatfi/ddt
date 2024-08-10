"""
Programmatically generated test function for Car.brake()
"""

import re
import pytest
from tests.oo_car import car

# Now import modules specific to Car.brake:
from logging import Logger
from tests.oo_car.car import Car


# In sum, these tests covered 71.43% of Car.brake's lines
# Line(s) not covered by ANY of the tests below:
# ['52']
@pytest.mark.parametrize(
    "test_class_instance, rate, duration, expected_result",
    [
        (Car("Red", 10, 0), -1, 1, "9"),
    ],
)
def test_car_brake(test_class_instance, rate, duration, expected_result):
    """
    Programmatically generated test function for Car.brake()
    """
    result = test_class_instance.brake(rate, duration)
    assert result == expected_result or result == eval(expected_result)
