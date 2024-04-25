import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 50.0% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# ['19', '43-49']
def test_fizzbuzz_0():
    monkeypatch = MonkeyPatch()

    # Coverage: 50.00% of function lines [19-52]
    # Covered Lines: 35-42;52
    # Lines not covered: 19-34;43-51
    # Note: Any lines not mentioned are comments or whitespace
    mode = "fizzbuzz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    args = []
    args.append(30)
    x = fizzbuzz.fizzbuzz(*args)
    assert x == "30 with mode='fizzbuzz' yields 'fizzbuzz'"
