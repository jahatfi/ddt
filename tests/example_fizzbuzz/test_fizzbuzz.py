"""
Programmatically generated test function for fizzbuzz
"""

import pytest
from tests.example_fizzbuzz import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch


# In sum, these tests covered 94.44% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# [23]
@pytest.mark.parametrize(
    "number, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            30,
            "N/A",
            "N/A",
            "N/A",
            "30 with mode='buzzfizz' yields 'buzzfizz'",
            "str",
            {"mode": "buzzfizz"},
            {},
        ),
        (
            30,
            "N/A",
            "N/A",
            "N/A",
            "30 with mode='fizzbuzz' yields 'fizzbuzz'",
            "str",
            {"mode": "fizzbuzz"},
            {},
        ),
        (
            6,
            "N/A",
            "N/A",
            "N/A",
            "Mode 'a_test' invalid for fizzbuzz()",
            "str",
            {"mode": "a_test"},
            {},
        ),
    ],
)
def test_fizzbuzz(
    number,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for fizzbuzz
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(fizzbuzz, k, v)
    x = fizzbuzz.fizzbuzz(number)
    assert x == result or repr(x) == result or repr(result) == x
