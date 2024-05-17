"""
Programmatically generated test function for Car.__init__
"""

import car


# In sum, these tests covered 75.0% of Car.__init__'s lines
# Line(s) not covered by ANY of the tests below:
# [33]
def test_car___init___0():
    """
    Programmatically generated test function for Car.__init__
    """
    # Coverage: 75.00% of function lines [33-43]
    # Covered Lines: 41-43
    # Lines not covered: 33-40
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append("Red")
    args.append(10)
    args.append(0)
    x = car.Car(*args)
    assert isinstance(x, car.Car)
