"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 43.75% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1549', '1567-1571', '1576-1578', '1583-1588', '1593-1596', '1598-1600', '1603', '1606-1609', '1614', '1617', '1622-1625', '1632-1633']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 43.75% of function lines [1549-1639]
    # Covered Lines: 1560-1562;1566;1573-1574;1580-1582;1591-1592;1597;1611-1612;1615-1616;1619-1621;1627-1631;1634;1637-1639
    # Lines not covered: 1549-1559;1567-1572;1576-1579;1583-1590;1593-1596;1598-1610;1614;1617-1618;1622-1626;1632-1633;1635-1636
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(
        CoverageInfo(
            parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
            args=[
                "0",
                '"error_code"',
                '"Before"',
                "CoverageInfo(parameter_names=['a', 'b'], args=['6', '2'], kwargs={}, globals_before={}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            ],
            kwargs={},
            globals_before={},
            globals_after={},
            result="CoverageInfo(parameter_names=['a', 'b'], args=['6', '2'], kwargs={}, globals_before={'error_code': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            coverage=[1400, 1403, 1407, 1411, 1412, 1415],
            exception_type="",
            exception_message="",
            constructor="",
            cost=0.001,
            result_type="src.unit_test_generator.CoverageInfo",
        )
    )
    args.append("  ")
    args.append("unit_test_generator")
    args.append("update_global")
    args.append("src.unit_test_generator.CoverageInfo")
    x = unit_test_generator.meta_program_function_call(*args)
    assert x == [
        "  x = unit_test_generator.update_global(*args)\n",
        "  assert x == CoverageInfo(parameter_names=['a', 'b'], args=['6', '2'], kwargs={}, globals_before={'error_code': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')\n",
    ]
