"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 43.75% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1550', '1568-1572', '1577-1579', '1584-1589', '1594-1597', '1599-1601', '1604', '1607-1610', '1615', '1618', '1623-1626', '1633-1634']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 43.75% of function lines [1550-1640]
    # Covered Lines: 1561-1563;1567;1574-1575;1581-1583;1592-1593;1598;1612-1613;1616-1617;1620-1622;1628-1632;1635;1638-1640
    # Lines not covered: 1550-1560;1568-1573;1577-1580;1584-1591;1594-1597;1599-1611;1615;1618-1619;1623-1627;1633-1634;1636-1637
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
            coverage=[1401, 1404, 1408, 1412, 1413, 1416],
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
