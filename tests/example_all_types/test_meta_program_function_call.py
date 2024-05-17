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
            args=["all_types.get_item_at_index"],
            kwargs={},
            globals_before={},
            globals_after={},
            result="[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            coverage=[
                1028,
                1030,
                1031,
                1032,
                1033,
                1034,
                1036,
                1037,
                1038,
                1039,
                1051,
                1052,
                1054,
                1057,
                1060,
                1070,
                1072,
                1074,
                1075,
                1076,
                1077,
                1078,
                1079,
                1080,
                1084,
                1085,
                1086,
                1087,
                1088,
                1089,
                1091,
                1095,
                1100,
            ],
            exception_type="",
            exception_message="",
            constructor="",
            cost=0.003,
            result_type="list",
        )
    )
    args.append("  ")
    args.append("unit_test_generator")
    args.append("return_function_line_numbers_and_accessed_globals")
    args.append("list")
    x = unit_test_generator.meta_program_function_call(*args)
    assert x == [
        "  x = unit_test_generator.return_function_line_numbers_and_accessed_globals(*args)\n",
        "  assert x == [[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]\n",
    ]
