import divide_ints
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 41.67% of divide_ints's lines
# Line(s) not covered by ANY of the tests below:
# ['17', '21-22', '24-25', '27-28']
def test_divide_ints_0():
    monkeypatch = MonkeyPatch()

    # Coverage: 41.67% of function lines [17-29]
    # Covered Lines: 19-20;23;26;29
    # Lines not covered: 17-18;21-22;24-25;27-28
    # Note: Any lines not mentioned are comments or whitespace
    error_code = 0
    monkeypatch.setattr(divide_ints, "error_code", error_code)
    args = []
    args.append(6)
    args.append(2)
    x = divide_ints.divide_ints(*args)
    assert x == "6/2=3.0"
    modified_error_code = 0
    assert divide_ints.__dict__.get("error_code") == modified_error_code
