"""
Programmatically generated test function for fizzbuzz
"""

from tests.example_fizzbuzz import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 94.44% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# [23]
def test_fizzbuzz_0():
    monkeypatch = MonkeyPatch()
    """
  Programmatically generated test function for fizzbuzz
  """
    # Coverage: 44.44% of function lines [23-57]
    # Covered Lines: 40-41;48-51;53;57
    # Lines not covered: 23-39;42-47;52;54-56
    # Note: Any lines not mentioned are comments or whitespace
    mode = "buzzfizz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    args = []
    args.append(6)
    x = fizzbuzz.fizzbuzz(*args)
    assert x == "6  with mode='buzzfizz' yields 'buzz'"


def test_fizzbuzz_1():
    monkeypatch = MonkeyPatch()
    """
  Programmatically generated test function for fizzbuzz
  """
    # Coverage: 55.56% of function lines [23-57]
    # Covered Lines: 40-41;48-54;57
    # Lines not covered: 23-39;42-47;56
    # Note: Any lines not mentioned are comments or whitespace
    mode = "buzzfizz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    args = []
    args.append(30)
    x = fizzbuzz.fizzbuzz(*args)
    assert x == "30 with mode='buzzfizz' yields 'buzzfizz'"


def test_fizzbuzz_2():
    monkeypatch = MonkeyPatch()
    """
  Programmatically generated test function for fizzbuzz
  """
    # Coverage: 38.89% of function lines [23-57]
    # Covered Lines: 40-44;46;57
    # Lines not covered: 23-39;45;47-56
    # Note: Any lines not mentioned are comments or whitespace
    mode = "fizzbuzz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    args = []
    args.append(6)
    x = fizzbuzz.fizzbuzz(*args)
    assert x == "6  with mode='fizzbuzz' yields 'fizz'"


def test_fizzbuzz_3():
    monkeypatch = MonkeyPatch()
    """
  Programmatically generated test function for fizzbuzz
  """
    # Coverage: 50.00% of function lines [23-57]
    # Covered Lines: 40-47;57
    # Lines not covered: 23-39;48-56
    # Note: Any lines not mentioned are comments or whitespace
    mode = "fizzbuzz"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    args = []
    args.append(30)
    x = fizzbuzz.fizzbuzz(*args)
    assert x == "30 with mode='fizzbuzz' yields 'fizzbuzz'"


def test_fizzbuzz_4():
    monkeypatch = MonkeyPatch()
    """
  Programmatically generated test function for fizzbuzz
  """
    # Coverage: 27.78% of function lines [23-57]
    # Covered Lines: 40-41;48;56-57
    # Lines not covered: 23-39;42-47;49-55
    # Note: Any lines not mentioned are comments or whitespace
    mode = "a_test"
    monkeypatch.setattr(fizzbuzz, "mode", mode)
    args = []
    args.append(6)
    x = fizzbuzz.fizzbuzz(*args)
    assert x == "Mode 'a_test' invalid for fizzbuzz()"
