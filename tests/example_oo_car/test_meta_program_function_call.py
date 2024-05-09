"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 50.0% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1543', '1561-1565', '1570-1572', '1577', '1582-1584', '1587', '1590-1593', '1598', '1601', '1606-1609', '1616-1617']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """
    # Coverage: 50.00% of function lines [1543-1623]
    # Covered Lines: 1554-1556;1560;1567-1568;1574-1576;1579;1581;1595-1596;1599-1600;1603-1605;1611-1615;1618;1621-1623
    # Lines not covered: 1543-1553;1561-1566;1570-1573;1577-1578;1582-1594;1598;1601-1602;1606-1610;1616-1617;1619-1620
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(
        CoverageInfo(
            args=[
                "0",
                '"method_call_counter"',
                '"Before"',
                "CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)')",
            ],
            kwargs={},
            globals_before={},
            globals_after={},
            result="CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)')",
            coverage=[1402, 1405, 1409, 1413, 1414, 1417],
            exception_type="",
            exception_message="",
            constructor="",
        )
    )
    args.append("  ")
    args.append("unit_test_generator")
    args.append("update_global")
    args.append("src.unit_test_generator.CoverageInfo")
    x = unit_test_generator.meta_program_function_call(*args)
    assert x == [
        "  x = unit_test_generator.update_global(*args)\n",
        "  assert x == CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)')\n",
    ]
