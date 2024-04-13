import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 38.89% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# ['36', '38-45', '15']
def test_fizzbuzz_0():
    monkeypatch = MonkeyPatch()

    # Coverage: 38.89% of function lines [15-48]
    # Covered Lines: 31-35;37;48
    # Lines not covered: 15-30;36;38-47
    # Note: Any lines not mentioned are comments or whitespace
    mode = "fizzbuzz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    args = []
    args.append(6)
    x = fizzbuzz.fizzbuzz(*args)
    assert x == "6  with mode='fizzbuzz' yields 'fizz'"
