"""
Programmatically generated test function for fizzbuzz
"""

from tests.example_fizzbuzz import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 94.44% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# [23]
def test_fizzbuzz_0():
    """
    Programmatically generated test function for fizzbuzz
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 55.56% of function lines [23-57]
    # Covered Lines: 40-41;48-54;57
    # Lines not covered: 23-39;42-47;56
    # Note: Any lines not mentioned are comments or whitespace
    mode = "buzzfizz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    x = fizzbuzz.fizzbuzz(30)
    assert x == "30 with mode='buzzfizz' yields 'buzzfizz'"


def test_fizzbuzz_1():
    """
    Programmatically generated test function for fizzbuzz
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 50.00% of function lines [23-57]
    # Covered Lines: 40-47;57
    # Lines not covered: 23-39;48-56
    # Note: Any lines not mentioned are comments or whitespace
    mode = "fizzbuzz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    x = fizzbuzz.fizzbuzz(30)
    assert x == "30 with mode='fizzbuzz' yields 'fizzbuzz'"


def test_fizzbuzz_2():
    """
    Programmatically generated test function for fizzbuzz
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 27.78% of function lines [23-57]
    # Covered Lines: 40-41;48;56-57
    # Lines not covered: 23-39;42-47;49-55
    # Note: Any lines not mentioned are comments or whitespace
    mode = "a_test"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    x = fizzbuzz.fizzbuzz(6)
    assert x == "Mode 'a_test' invalid for fizzbuzz()"
