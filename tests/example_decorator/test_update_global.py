"""
Programmatically generated test function for update_global()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 46.15% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1539-1540', '1522-1523', '1525-1527']
@pytest.mark.parametrize(
    "obj, this_global, phase, this_coverage_info, expected_result, expected_type, args_after",
    [
        (
            [5],
            "c",
            "Before",
            CoverageInfo(
                args_before=["2", "7"],
                args_after={},
                kwargs={},
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
            "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
            CoverageInfo,
            {
                "obj": "[5]",
                "this_coverage_info": "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
            },
        ),
    ],
)
def test_update_global(
    obj,
    this_global,
    phase,
    this_coverage_info,
    expected_result,
    expected_type,
    args_after,
):
    """
    Programmatically generated test function for update_global()
    """
    result = unit_test_generator.update_global(
        obj, this_global, phase, this_coverage_info
    )
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
    assert args_after["obj"] == obj or obj == eval(args_after["obj"])
    assert args_after[
        "this_coverage_info"
    ] == this_coverage_info or this_coverage_info == eval(
        args_after["this_coverage_info"]
    )
