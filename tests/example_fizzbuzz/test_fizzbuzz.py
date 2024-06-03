"""
Programmatically generated test function for fizzbuzz()
"""

import pytest
from tests.example_fizzbuzz import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 94.44% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# [23]
@pytest.mark.parametrize(
    "number, expected_result, expected_type, globals_before",
    [
        (30, "30 with mode='fizzbuzz' yields 'fizzbuzz'", str, {"mode": "fizzbuzz"}),
        (30, "30 with mode='buzzfizz' yields 'buzzfizz'", str, {"mode": "buzzfizz"}),
        (6, "Mode 'a_test' invalid for fizzbuzz()", str, {"mode": "a_test"}),
    ],
)
def test_fizzbuzz(number, expected_result, expected_type, globals_before):
    """
    Programmatically generated test function for fizzbuzz()
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(fizzbuzz, k, v)
    result = fizzbuzz.fizzbuzz(number)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
