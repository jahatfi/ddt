"""
Programmatically generated test function for normalize_arg
"""

from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1417', '1426', '1428']
def test_normalize_arg_0():
    """
    Programmatically generated test function for normalize_arg
    """

    # Coverage: 60.00% of function lines [1417-1432]
    # Covered Lines: 1423-1425;1427;1430;1432
    # Lines not covered: 1417-1422;1426;1428-1429;1431
    # Note: Any lines not mentioned are comments or whitespace
    arg = "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]"
    x = unit_test_generator.normalize_arg(arg)
    assert x == "[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]"
