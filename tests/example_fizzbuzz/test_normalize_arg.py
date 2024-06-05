"""
Programmatically generated test function for normalize_arg
"""

from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1440', '1426', '1435']
def test_normalize_arg_0():
    """
    Programmatically generated test function for normalize_arg
    """

    # Coverage: 60.00% of function lines [1426-1441]
    # Covered Lines: 1432-1434;1436;1439;1441
    # Lines not covered: 1426-1431;1435;1437-1438;1440
    # Note: Any lines not mentioned are comments or whitespace
    arg = "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')"
    x = unit_test_generator.normalize_arg(arg)
    assert (
        x
        == "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')"
    )
