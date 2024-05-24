"""
Programmatically generated test function for update_global
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 54.55% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1409', '1414-1415', '1393']
@pytest.mark.parametrize(
    "obj,this_global,phase,this_coverage_info, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
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
            "N/A",
            "N/A",
            "N/A",
            "CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            "src.unit_test_generator.CoverageInfo",
            {},
            {},
        ),
    ],
)
def test_update_global(
    obj,
    this_global,
    phase,
    this_coverage_info,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for update_global
    """
    x = unit_test_generator.update_global(obj, this_global, phase, this_coverage_info)
    assert x == result
