"""
Programmatically generated test function for fizzbuzz
"""

import pytest
import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 94.44% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# [23]
@pytest.mark.parametrize(
    "number, result, return_type, globals_before",
    [
        (30, "30 with mode='fizzbuzz' yields 'fizzbuzz'", str, {"mode": "fizzbuzz"}),
        (30, "30 with mode='buzzfizz' yields 'buzzfizz'", str, {"mode": "buzzfizz"}),
        (6, "Mode 'a_test' invalid for fizzbuzz()", str, {"mode": "a_test"}),
    ],
)
def test_fizzbuzz(number, result, return_type, globals_before):
    """
    Programmatically generated test function for fizzbuzz
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(fizzbuzz, k, v)
    x = fizzbuzz.fizzbuzz(number)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
