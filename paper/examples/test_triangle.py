import example as module0

def test_case_0():
    int_0 = 4271
    int_1 = -3706
    str_0 = module0.triangle(int_0, int_0, int_1)
    assert str_0 == "Isosceles triangle"

def test_case_1():
    int_0 = -163
    int_1 = 484
    int_2 = 77
    str_0 = module0.triangle(int_0, int_1, int_2)
    assert str_0 == "Scalene triangle"
