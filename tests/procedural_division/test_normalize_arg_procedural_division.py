"""
Programmatically generated test function for normalize_arg()
"""

import pytest
from src import unit_test_generator


# In sum, these tests covered 50.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1730', '1732', '1734', '1737-1738']
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "arg, expected_result",
    [
        (-1, "-1"),
    ],
    ids=counter,
)
def test_normalize_arg(arg, expected_result):
    """
    Programmatically generated test function for normalize_arg()
    """
    result = unit_test_generator.normalize_arg(arg)
    assert result == expected_result or result == eval(expected_result)
