"""
Programmatically generated test function for update_global()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 50.0% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1445-1446', '1428-1429', '1431-1432']
@pytest.mark.parametrize(
    "obj, this_global, phase, this_coverage_info, expected_result, expected_type",
    [
        (
            0,
            "method_call_counter",
            "Before",
            CoverageInfo(
                args=["-1", "1"],
                kwargs={},
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
            "CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
            CoverageInfo,
        ),
    ],
)
def test_update_global(
    obj, this_global, phase, this_coverage_info, expected_result, expected_type
):
    """
    Programmatically generated test function for update_global()
    """
    result = unit_test_generator.update_global(
        obj, this_global, phase, this_coverage_info
    )
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
