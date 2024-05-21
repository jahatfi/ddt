"""
Programmatically generated test function for meta_program_function_call
"""

from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 45.59% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1538', '1556-1560', '1565-1567', '1572-1579', '1583', '1587-1588', '1591-1593', '1596', '1599-1602', '1607', '1610', '1615-1618', '1625-1626']
def test_meta_program_function_call_0():
    """
    Programmatically generated test function for meta_program_function_call
    """

    # Coverage: 45.59% of function lines [1538-1632]
    # Covered Lines: 1549-1551;1555;1562-1563;1569-1571;1582;1584-1586;1589-1590;1604-1605;1608-1609;1612-1614;1620-1624;1627;1630-1632
    # Lines not covered: 1538-1548;1556-1561;1565-1568;1572-1581;1583;1587-1588;1591-1603;1607;1610-1611;1615-1619;1625-1626;1628-1629
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
        "  x = unit_test_generator.return_function_line_numbers_and_accessed_globals(all_types.get_item_at_index)\n",
        "  assert x == [[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]\n",
    ]
