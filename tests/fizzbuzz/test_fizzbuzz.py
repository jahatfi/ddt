"""
Programmatically generated test function for fizzbuzz()
"""

import re
import pytest
from collections import OrderedDict
import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 100.0% of fizzbuzz's lines
@pytest.mark.parametrize(
    "number, expected_result, globals_before",
    "number, expected_result, globals_before",
    [
        (6, "Mode 'a_test' invalid for fizzbuzz()", {"mode": "a_test"}),
        (30, "30 with mode='buzzfizz' yields 'buzzfizz'", {"mode": "buzzfizz"}),
        (30, "30 with mode='fizzbuzz' yields 'fizzbuzz'", {"mode": "fizzbuzz"}),
    ],
)
def test_fizzbuzz(number, expected_result, globals_before):
def test_fizzbuzz(number, expected_result, globals_before):
    """
    Programmatically generated test function for fizzbuzz()
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(fizzbuzz, k, v)
    result = fizzbuzz.fizzbuzz(number)
    assert result == expected_result or result == eval(expected_result)
