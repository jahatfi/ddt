"""
Programmatically generated test function for Car.brake
"""

import pytest

# Now import modules specific to Car.brake:
from car import Car


# In sum, these tests covered 62.5% of Car.brake's lines
# Line(s) not covered by ANY of the tests below:
# ['45', '52']
@pytest.mark.parametrize(
    "test_class_instance, rate, duration, result, return_type",
    [
        (Car("Red", 10, 0), -1, 1, "9", int),
    ],
)
def test_car_brake(test_class_instance, rate, duration, result, return_type):
    """
    Programmatically generated test function for Car.brake
    """
    x = test_class_instance.brake(rate, duration)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
