"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 48.44% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1550', '1568-1572', '1577-1579', '1584-1589', '1593', '1599-1601', '1604', '1607-1610', '1615', '1618', '1623-1626', '1633-1634']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 48.44% of function lines [1550-1640]
    # Covered Lines: 1561-1563;1567;1574-1575;1581-1583;1592;1594-1598;1612-1613;1616-1617;1620-1622;1628-1632;1635;1638-1640
    # Lines not covered: 1550-1560;1568-1573;1577-1580;1584-1591;1593;1599-1611;1615;1618-1619;1623-1627;1633-1634;1636-1637
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
                1032,
                1034,
                1035,
                1036,
                1037,
                1038,
                1040,
                1041,
                1042,
                1043,
                1055,
                1056,
                1058,
                1061,
                1064,
                1074,
                1076,
                1078,
                1079,
                1080,
                1081,
                1082,
                1083,
                1084,
                1088,
                1089,
                1090,
                1091,
                1092,
                1093,
                1095,
                1099,
                1104,
            ],
            exception_type="",
            exception_message="",
            constructor="",
            cost=0.002,
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
