from tests.example_all_types import all_types
import pytest


# In sum, these tests covered 75.0% of get_item_at_index's lines
# Line(s) not covered by ANY of the tests below:
# ['17']
def test_get_item_at_index_0():
    # Coverage: 50.00% of function lines [17-31]
    # Covered Lines: 24;26;28-29
    # Lines not covered: 17-23;25;27;31
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append("a test string")
    args.append(-5)
    with pytest.raises(
        ValueError, match=r"index\ must\ be\ in\ range\ \[0,\ 12\],\ was\ \-5"
    ):
        all_types.get_item_at_index(*args)


def test_get_item_at_index_1():
    # Coverage: 37.50% of function lines [17-31]
    # Covered Lines: 24;26-27
    # Lines not covered: 17-23;25;28-31
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append((5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    args.append(50)
    with pytest.raises(
        ValueError, match=r"index\ must\ be\ in\ range\ \[0,\ 9\],\ was\ 50"
    ):
        all_types.get_item_at_index(*args)


def test_get_item_at_index_2():
    # Coverage: 50.00% of function lines [17-31]
    # Covered Lines: 24;26;28;31
    # Lines not covered: 17-23;25;27;29-30
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append([-1, -2, -3, -4])
    args.append(0)
    x = all_types.get_item_at_index(*args)
    assert x == -1
