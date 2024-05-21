"""
Programmatically generated test function for Car.is_going_faster_than
"""


# Now import modules specific to Car.is_going_faster_than:
from car import Car


# In sum, these tests covered 50.0% of Car.is_going_faster_than's lines
# Line(s) not covered by ANY of the tests below:
# [117]
def test_car_is_going_faster_than_0():
    """
    Programmatically generated test function for Car.is_going_faster_than
    """

    # Coverage: 50.00% of function lines [117-123]
    # Covered Lines: 123
    # Lines not covered: 117-122
    # Note: Any lines not mentioned are comments or whitespace
    this_class = Car("Red", 20, 0)
    x = this_class.is_going_faster_than(Car("White", 19, 0))
    assert x is True
