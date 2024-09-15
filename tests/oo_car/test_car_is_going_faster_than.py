"""
Programmatically generated test function for Car.is_going_faster_than()
"""

import re
import pytest
from collections import OrderedDict
import car

# Now import modules specific to Car.is_going_faster_than:
from car import Car


# In sum, these tests covered 100.0% of Car.is_going_faster_than's lines
@pytest.mark.parametrize(
    "test_class_instance, other_car, expected_result, args_after",
    [
        (
            Car("Red", 20, 0),
            Car("White", 19, 0),
            "True",
            {"other_car": 'Car("White", 19, 0)'},
        ),
    ],
)
def test_car_is_going_faster_than(
    test_class_instance, other_car, expected_result, args_after
):
    """
    Programmatically generated test function for Car.is_going_faster_than()
    """
    result = test_class_instance.is_going_faster_than(other_car)
    assert result == expected_result or result == eval(expected_result)
    assert (
        other_car == eval(args_after["other_car"])
        or args_after["other_car"] == other_car
    )
