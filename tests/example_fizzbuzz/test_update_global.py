"""
Programmatically generated test function for update_global
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 46.67% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1412-1413', '1415-1416', '1429-1430', '1433']
@pytest.mark.parametrize(
    "obj, this_global, phase, this_coverage_info, result, return_type",
    [
        (
            "fizzbuzz",
            "mode",
            "Before",
            CoverageInfo(
                args=["6"],
                kwargs={},
                globals_before={},
                globals_after={},
                result="",
                coverage=[],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.0,
                result_type="",
            ),
            "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            CoverageInfo,
        ),
    ],
)
def test_update_global(
    obj, this_global, phase, this_coverage_info, result, return_type
):
    """
    Programmatically generated test function for update_global
    """
    x = unit_test_generator.update_global(obj, this_global, phase, this_coverage_info)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
