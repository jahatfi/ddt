"""
Programmatically generated test function for Car.brake()
"""

import pytest

# Now import modules specific to Car.brake:
from tests.oo_car.car import Car


# In sum, these tests covered 71.43% of Car.brake's lines
# Line(s) not covered by ANY of the tests below:
# ['55']
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "test_class_instance, rate, duration, expected_result",
    [
        (Car("Red", 10, 0), -1, 1, "9"),
    ],
    ids=counter,
)
def test_car_brake(test_class_instance, rate, duration, expected_result):
    """
    Programmatically generated test function for Car.brake()
    """
    result = test_class_instance.brake(rate, duration)
    assert result == expected_result or result == eval(expected_result)
