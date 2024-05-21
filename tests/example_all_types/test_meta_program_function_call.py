"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 48.44% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1546', '1564-1568', '1573-1575', '1580-1585', '1589', '1595-1597', '1600', '1603-1606', '1611', '1614', '1619-1622', '1629-1630']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 48.44% of function lines [1546-1636]
    # Covered Lines: 1557-1559;1563;1570-1571;1577-1579;1588;1590-1594;1608-1609;1612-1613;1616-1618;1624-1628;1631;1634-1636
    # Lines not covered: 1546-1556;1564-1569;1573-1576;1580-1587;1589;1595-1607;1611;1614-1615;1619-1623;1629-1630;1632-1633
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
        "  arg = all_types.get_item_at_index\n",
        "  x = unit_test_generator.return_function_line_numbers_and_accessed_globals(arg)\n",
        "  assert x == [[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]\n",
    ]
