"""
Programmatically generated test function for update_global
"""

from src import unit_test_generator

# Now import modules specific to update_global:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 54.55% of update_global's lines
# Line(s) not covered by ANY of the tests below:
# ['1409', '1414-1415', '1393']
def test_update_global_0():
    """
    Programmatically generated test function for update_global
    """

    # Coverage: 54.55% of function lines [1393-1416]
    # Covered Lines: 1401;1404;1408;1412-1413;1416
    # Lines not covered: 1393-1400;1402-1403;1409-1411;1414-1415
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
