"""
Programmatically generated test function for update_global()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 46.15% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1572-1573', '1575-1577', '1589-1590']
@pytest.mark.parametrize(
    "obj, this_global, phase, this_coverage_info, expected_result, args_after",
    [
        (
            0,
            "method_call_counter",
            "Before",
            CoverageInfo(
                args_before=["-1", "1"],
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
                constructor='Car("Red", 10, 0)',
                cost=0.0,
            ),
            "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
            {
                "this_coverage_info": "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)"
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
