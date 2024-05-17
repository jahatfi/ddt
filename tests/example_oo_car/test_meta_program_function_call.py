"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 50.0% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1538', '1556-1560', '1565-1567', '1572', '1577-1579', '1582', '1585-1588', '1593', '1596', '1601-1604', '1611-1612']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """
    # Coverage: 50.00% of function lines [1538-1618]
    # Covered Lines: 1549-1551;1555;1562-1563;1569-1571;1574;1576;1590-1591;1594-1595;1598-1600;1606-1610;1613;1616-1618
    # Lines not covered: 1538-1548;1556-1561;1565-1568;1572-1573;1577-1589;1593;1596-1597;1601-1605;1611-1612;1614-1615
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(
        CoverageInfo(
            args=[
                "0",
                '"method_call_counter"',
                '"Before"',
                "CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0, result_type='')",
            ],
            kwargs={},
            globals_before={},
            globals_after={},
            result="CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0, result_type='')",
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
        "  assert x == CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0, result_type='')\n",
    ]
