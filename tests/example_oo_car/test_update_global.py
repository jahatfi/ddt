"""
Programmatically generated test function for update_global
"""

from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 54.55% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1408', '1413-1414', '1392']
def test_update_global_0():
    """
    Programmatically generated test function for update_global
    """

    # Coverage: 54.55% of function lines [1392-1415]
    # Covered Lines: 1400;1403;1407;1411-1412;1415
    # Lines not covered: 1392-1399;1401-1402;1408-1410;1413-1414
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(0)
    args.append("method_call_counter")
    args.append("Before")
    args.append(
        CoverageInfo(
            parameter_names=["self", "rate", "duration"],
            args=["-1", "1"],
            kwargs={},
            globals_before={},
            globals_after={},
            result="",
            coverage=[],
            exception_type="",
            exception_message="",
            constructor='Car("Red", 10, 0)',
            cost=0.0,
            result_type="",
        )
    )
    x = unit_test_generator.update_global(*args)
    assert x == CoverageInfo(
        parameter_names=["self", "rate", "duration"],
        args=["-1", "1"],
        kwargs={},
        globals_before={"method_call_counter": "0"},
        globals_after={},
        result="",
        coverage=[],
        exception_type="",
        exception_message="",
        constructor='Car("Red", 10, 0)',
        cost=0.0,
        result_type="",
    )
