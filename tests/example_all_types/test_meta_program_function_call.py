"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 48.44% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1549', '1567-1571', '1576-1578', '1583-1588', '1592', '1598-1600', '1603', '1606-1609', '1614', '1617', '1622-1625', '1632-1633']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 48.44% of function lines [1549-1639]
    # Covered Lines: 1560-1562;1566;1573-1574;1580-1582;1591;1593-1597;1611-1612;1615-1616;1619-1621;1627-1631;1634;1637-1639
    # Lines not covered: 1549-1559;1567-1572;1576-1579;1583-1590;1592;1598-1610;1614;1617-1618;1622-1626;1632-1633;1635-1636
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append(
        CoverageInfo(
            parameter_names=["f"],
            args=["all_types.get_item_at_index"],
            kwargs={},
            globals_before={},
            globals_after={},
            result="[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            coverage=[
                1031,
                1033,
                1034,
                1035,
                1036,
                1037,
                1039,
                1040,
                1041,
                1042,
                1054,
                1055,
                1057,
                1060,
                1063,
                1073,
                1075,
                1077,
                1078,
                1079,
                1080,
                1081,
                1082,
                1083,
                1087,
                1088,
                1089,
                1090,
                1091,
                1092,
                1094,
                1098,
                1103,
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
