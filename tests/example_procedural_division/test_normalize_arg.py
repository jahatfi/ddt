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
    x = unit_test_generator.normalize_arg(
        "CoverageInfo(args=['6', '2'], kwargs={}, globals_before={'error_code': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')"
    )
    assert (
        x
        == "CoverageInfo(args=['6', '2'], kwargs={}, globals_before={'error_code': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')"
    )
