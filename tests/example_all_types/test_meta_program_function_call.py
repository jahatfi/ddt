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
            args=["all_types.get_item_at_index"],
            kwargs={},
            globals_before={},
            globals_after={},
            result="[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
            coverage=[
                1034,
                1036,
                1037,
                1038,
                1039,
                1040,
                1042,
                1043,
                1044,
                1045,
                1057,
                1058,
                1060,
                1063,
                1066,
                1076,
                1078,
                1080,
                1081,
                1082,
                1083,
                1084,
                1085,
                1086,
                1090,
                1091,
                1092,
                1093,
                1094,
                1095,
                1097,
                1101,
                1106,
            ],
            exception_type="",
            exception_message="",
            constructor="",
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
