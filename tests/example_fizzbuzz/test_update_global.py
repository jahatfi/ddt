"""
Programmatically generated test function for update_global()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 46.15% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1571-1572', '1574-1576', '1588-1589']
@pytest.mark.parametrize(
    "obj, this_global, phase, this_coverage_info, expected_result, args_after",
    [
        (
            "fizzbuzz",
            "mode",
            "Before",
            CoverageInfo(
                args_before=["6"],
                args_after={},
                kwargs={},
                kwargs_after={},
                globals_before={},
                globals_after={},
                expected_result="",
                expected_type="",
                coverage=[],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.0,
            ),
            "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
            {
                "this_coverage_info": "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)"
            },
        ),
    ],
)
def test_update_global(
    obj, this_global, phase, this_coverage_info, expected_result, args_after
):
    """
    Programmatically generated test function for update_global()
    """
    result = unit_test_generator.update_global(
        obj, this_global, phase, this_coverage_info
    )
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_coverage_info == eval(args_after["this_coverage_info"])
        or args_after["this_coverage_info"] == this_coverage_info
    )
