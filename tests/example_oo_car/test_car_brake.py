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
    "self,rate,duration, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (-1, 1, "N/A", "N/A", "N/A", "9", "int", {}, {}),
    ],
)
def test_car_brake(
    self,
    rate,
    duration,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for Car.brake
    """
    this_class = Car("Red", 10, 0)
    x = this_class.brake(self, rate, duration)
    assert x == result or repr(x) == result or repr(result) == x
