"""
Programmatically generated test function for update_global
"""

from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 54.55% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1410-1411', '1389', '1398']
def test_update_global_0():
    """
    Programmatically generated test function for update_global
    """
    # Coverage: 54.55% of function lines [1389-1412]
    # Covered Lines: 1397;1400;1404;1408-1409;1412
    # Lines not covered: 1389-1396;1398-1399;1405-1407;1410-1411
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append("fizzbuzz")
    args.append("mode")
    args.append("Before")
    args.append(
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
        )
    )
    x = unit_test_generator.update_global(*args)
    assert x == CoverageInfo(
        args=["6"],
        kwargs={},
        globals_before={"mode": "'fizzbuzz'"},
        globals_after={},
        result="",
        coverage=[],
        exception_type="",
        exception_message="",
        constructor="",
        cost=0.0,
        result_type="",
    )
