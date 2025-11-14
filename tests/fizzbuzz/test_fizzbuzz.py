"""
Programmatically generated test function for fizzbuzz()
"""

import pytest
import fizzbuzz
from _pytest.monkeypatch import MonkeyPatch

MODE = "fizzbuzz"


# In sum, these tests covered 52.94% of fizzbuzz's lines
# Line(s) not covered by ANY of the tests below:
# ['41-47']
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "number, expected_result",
    [
        (30, "30 with mode='fizzbuzz' yields 'fizzbuzz'"),
    ],
    ids=counter,
)
def test_fizzbuzz(number, expected_result):
    """
    Programmatically generated test function for fizzbuzz()
    """
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr(fizzbuzz, "mode", MODE)
    result = fizzbuzz.fizzbuzz(number)
    assert result == expected_result or result == eval(expected_result)
