"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 43.75% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1546', '1564-1568', '1573-1575', '1580-1585', '1590-1593', '1595-1597', '1600', '1603-1606', '1611', '1614', '1619-1622', '1629-1630']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 43.75% of function lines [1546-1636]
    # Covered Lines: 1557-1559;1563;1570-1571;1577-1579;1588-1589;1594;1608-1609;1612-1613;1616-1618;1624-1628;1631;1634-1636
    # Lines not covered: 1546-1556;1564-1569;1573-1576;1580-1587;1590-1593;1595-1607;1611;1614-1615;1619-1623;1629-1630;1632-1633
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(
        CoverageInfo(
            args=[
                '"fizzbuzz"',
                '"mode"',
                '"Before"',
                "CoverageInfo(args=['6'], kwargs={}, globals_before={}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
            ],
            kwargs={},
            globals_before={},
            globals_after={},
            result="CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
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
        "  assert x == CoverageInfo(args=['6'], kwargs={}, globals_before={'mode': \"'fizzbuzz'\"}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')\n",
    ]
