"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 48.44% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1555', '1573-1577', '1582-1584', '1589-1594', '1598', '1604-1606', '1609', '1612-1615', '1620', '1623', '1628-1631', '1638-1639']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 48.44% of function lines [1555-1645]
    # Covered Lines: 1566-1568;1572;1579-1580;1586-1588;1597;1599-1603;1617-1618;1621-1622;1625-1627;1633-1637;1640;1643-1645
    # Lines not covered: 1555-1565;1573-1578;1582-1585;1589-1596;1598;1604-1616;1620;1623-1624;1628-1632;1638-1639;1641-1642
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
                1037,
                1039,
                1040,
                1041,
                1042,
                1043,
                1045,
                1046,
                1047,
                1048,
                1060,
                1061,
                1063,
                1066,
                1069,
                1079,
                1081,
                1083,
                1084,
                1085,
                1086,
                1087,
                1088,
                1089,
                1093,
                1094,
                1095,
                1096,
                1097,
                1098,
                1100,
                1104,
                1109,
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
