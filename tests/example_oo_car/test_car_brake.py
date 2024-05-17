"""
Programmatically generated test function for Car.brake
"""


# Now import modules specific to Car.brake:
from car import Car


# In sum, these tests covered 62.5% of Car.brake's lines
# Line(s) not covered by ANY of the tests below:
# ['45', '52']
def test_car_brake_0():
    """
    Programmatically generated test function for Car.brake
    """
    # Coverage: 62.50% of function lines [45-56]
    # Covered Lines: 50-51;53;55-56
    # Lines not covered: 45-49;52;54
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(-1)
    args.append(1)
    this_class = Car("Red", 10, 0)
    x = this_class.brake(*args)
    assert x == 9
