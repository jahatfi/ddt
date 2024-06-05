"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 43.75% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1555', '1573-1577', '1582-1584', '1589-1594', '1599-1602', '1604-1606', '1609', '1612-1615', '1620', '1623', '1628-1631', '1638-1639']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 43.75% of function lines [1555-1645]
    # Covered Lines: 1566-1568;1572;1579-1580;1586-1588;1597-1598;1603;1617-1618;1621-1622;1625-1627;1633-1637;1640;1643-1645
    # Lines not covered: 1555-1565;1573-1578;1582-1585;1589-1596;1599-1602;1604-1616;1620;1623-1624;1628-1632;1638-1639;1641-1642
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
            coverage=[1406, 1409, 1413, 1417, 1418, 1421],
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
