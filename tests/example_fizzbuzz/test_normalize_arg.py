"""
Programmatically generated test function for normalize_arg
"""

from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1422', '1431', '1433']
def test_normalize_arg_0():
    """
    Programmatically generated test function for normalize_arg
    """
    # Coverage: 60.00% of function lines [1422-1437]
    # Covered Lines: 1428-1430;1432;1435;1437
    # Lines not covered: 1422-1427;1431;1433-1434;1436
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(
        "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='')"
    )
    x = unit_test_generator.normalize_arg(*args)
    assert (
        x
        == "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='')"
    )
