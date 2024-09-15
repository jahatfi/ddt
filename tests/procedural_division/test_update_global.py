"""
Programmatically generated test function for update_global()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to update_global:
from logging import StreamHandler
from src.unit_test_generator import CoverageInfo
from logging import Logger
from logging import RootLogger
from logging import PlaceHolder
from logging import Manager


# In sum, these tests covered 46.15% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1697-1698', '1700-1702', '1714-1715']
@pytest.mark.parametrize(
    "obj, this_global, phase, this_coverage_info, expected_result, args_after",
    [
        (
            0,
            "error_code",
            "Before",
            CoverageInfo(
                args_before=["6", "2"],
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
                testable=0.0,
            ),
            "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, testable=0.0)",
            {
                "obj": "0",
                "this_global": '"error_code"',
                "phase": '"Before"',
                "this_coverage_info": "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, testable=0.0)",
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
    assert obj == eval(args_after["obj"]) or args_after["obj"] == obj
    assert (
        this_global == eval(args_after["this_global"])
        or args_after["this_global"] == this_global
    )
    assert phase == eval(args_after["phase"]) or args_after["phase"] == phase
    assert (
        this_coverage_info == eval(args_after["this_coverage_info"])
        or args_after["this_coverage_info"] == this_coverage_info
    )
