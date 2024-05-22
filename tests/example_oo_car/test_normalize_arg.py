"""
Programmatically generated test function for normalize_arg
"""

from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1420', '1429', '1431']
def test_normalize_arg_0():
    """
    Programmatically generated test function for normalize_arg
    """

    # Coverage: 60.00% of function lines [1420-1435]
    # Covered Lines: 1426-1428;1430;1433;1435
    # Lines not covered: 1420-1425;1429;1431-1432;1434
    # Note: Any lines not mentioned are comments or whitespace
    arg = "CoverageInfo(parameter_names=['self', 'rate', 'duration'], args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0, result_type='')"
    x = unit_test_generator.normalize_arg(arg)
    assert (
        x
        == "CoverageInfo(parameter_names=['self', 'rate', 'duration'], args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0, result_type='')"
    )
