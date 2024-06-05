"""
Programmatically generated test function for update_global
"""

from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 54.55% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1414', '1419-1420', '1398']
def test_update_global_0():
    """
    Programmatically generated test function for update_global
    """

    # Coverage: 54.55% of function lines [1398-1421]
    # Covered Lines: 1406;1409;1413;1417-1418;1421
    # Lines not covered: 1398-1405;1407-1408;1414-1416;1419-1420
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(0)
    args.append("method_call_counter")
    args.append("Before")
    args.append(
        CoverageInfo(
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
