"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 41.18% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1538', '1556-1560', '1565-1567', '1572-1579', '1584-1589', '1591-1593', '1596', '1599-1602', '1607', '1610', '1615-1618', '1625-1626']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 41.18% of function lines [1538-1632]
    # Covered Lines: 1549-1551;1555;1562-1563;1569-1571;1582-1583;1590;1604-1605;1608-1609;1612-1614;1620-1624;1627;1630-1632
    # Lines not covered: 1538-1548;1556-1561;1565-1568;1572-1581;1584-1589;1591-1603;1607;1610-1611;1615-1619;1625-1626;1628-1629
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(
        CoverageInfo(
            args=[
                "0",
                '"error_code"',
                '"Before"',
                "CoverageInfo(args=['6', '2'], kwargs={}, globals_before={}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            ],
            kwargs={},
            globals_before={},
            globals_after={},
            result="CoverageInfo(args=['6', '2'], kwargs={}, globals_before={'error_code': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            coverage=[1397, 1400, 1404, 1408, 1409, 1412],
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
        "  assert x == CoverageInfo(args=['6', '2'], kwargs={}, globals_before={'error_code': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')\n",
    ]
