"""
Programmatically generated test function for normalize_arg
"""

import pytest
from src import unit_test_generator


# In sum, these tests covered 60.0% of normalize_arg's lines
# Line(s) not covered by ANY of the tests below:
# ['1448', '1450', '1453']
@pytest.mark.parametrize(
    "arg, result, return_type",
    [
        (
            "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            str,
        ),
    ],
)
def test_normalize_arg(arg, result, return_type):
    """
    Programmatically generated test function for normalize_arg
    """
    x = unit_test_generator.normalize_arg(arg)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
