import car


# In sum, these tests covered 75.0% of Car.__init__'s lines
# Line(s) not covered by ANY of the tests below:
# [25]
def test_Car___init___0():
    # Coverage: 75.00% of function lines [25-33]
    # Covered Lines: 31-33
    # Lines not covered: 25-30
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append("Red")
    args.append(10)
    args.append(0)
    x = car.Car(*args)
    assert isinstance(x, car.Car)
