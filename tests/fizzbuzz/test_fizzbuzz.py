"""
Programmatically generated test function for fizzbuzz()
"""

import pytest
from tests.fizzbuzz import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 100.0% of fizzbuzz's lines
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "number, expected_result, globals_before",
    [
        (6, "Mode 'a_test' invalid for fizzbuzz()", {"mode": "a_test"}),
        (30, "30 with mode='buzzfizz' yields 'buzzfizz'", {"mode": "buzzfizz"}),
        (30, "30 with mode='fizzbuzz' yields 'fizzbuzz'", {"mode": "fizzbuzz"}),
    ],
    ids=counter,
)
def test_fizzbuzz(number, expected_result, globals_before):
    """
    Programmatically generated test function for fizzbuzz()
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(fizzbuzz, k, v)
    result = fizzbuzz.fizzbuzz(number)
    assert result == expected_result or result == eval(expected_result)
