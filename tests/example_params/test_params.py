"""
Asserts a right triangle
"""
import pytest

@pytest.mark.parametrize(
    "a,b,c",
    [
        (3,4,5),
        (95,168,193)
    ],
)
def test_is_right_triangle(a:int, b:int, c:int):
    """Asserts a right triangle"""
    assert a >= 0
    assert b > 0
    assert a**2 + b**2 == c**2
