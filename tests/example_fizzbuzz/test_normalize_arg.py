"""
Programmatically generated test function for normalize_arg
"""

from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1421', '1430', '1432']
def test_normalize_arg_0():
    """
    Programmatically generated test function for normalize_arg
    """

    # Coverage: 60.00% of function lines [1421-1436]
    # Covered Lines: 1427-1429;1431;1434;1436
    # Lines not covered: 1421-1426;1430;1432-1433;1435
    # Note: Any lines not mentioned are comments or whitespace
    arg = "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')"
    x = unit_test_generator.normalize_arg(arg)
    assert (
        x
        == "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')"
    )
