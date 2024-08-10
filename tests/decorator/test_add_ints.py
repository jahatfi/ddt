"""
Programmatically generated test function for add_ints()
"""

import pytest
from tests.example_decorator import decorator
from _pytest.monkeypatch import MonkeyPatch

C = [5]


# In sum, these tests covered 100.0% of add_ints's lines
@pytest.mark.parametrize(
    "a, b, expected_result, expected_type, globals_before",
    [
        (2, 7, "14", int, {}),
    ],
)
def test_add_ints(a, b, expected_result, expected_type, globals_before):
    """
    Programmatically generated test function for add_ints()
    """
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr(decorator, "c", C)
    result = decorator.add_ints(a, b)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
