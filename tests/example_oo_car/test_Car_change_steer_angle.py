import car

# Now import modules specific to Car.change_steer_angle:
from car import Car


# In sum, these tests covered 45.45% of Car.change_steer_angle's lines
# Line(s) not covered by ANY of the tests below:
# ['68', '74-75']
def test_Car_change_steer_angle_0():
    # Coverage: 45.45% of function lines [60-77]
    # Covered Lines: 66-67;70;73;77
    # Lines not covered: 60-65;68-69;74-76
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(30)
    this_class = Car("Red", 10, 0)
    x = this_class.change_steer_angle(*args)
    assert x == 30
