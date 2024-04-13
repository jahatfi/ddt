import car

# Now import modules specific to Car.is_going_faster_than:
from car import Car


# In sum, these tests covered 50.0% of Car.is_going_faster_than's lines
# Line(s) not covered by ANY of the tests below:
# [94]
def test_Car_is_going_faster_than_0():
    # Coverage: 50.00% of function lines [94-100]
    # Covered Lines: 100
    # Lines not covered: 94-99
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(Car("White", 19, 0))
    this_class = Car("Red", 20, 0)
    x = this_class.is_going_faster_than(*args)
    assert x == True
