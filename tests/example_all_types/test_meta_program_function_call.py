"""
Programmatically generated test function for meta_program_function_call
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 52.11% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1568', '1594-1595', '1602-1604', '1608-1610', '1613', '1617', '1625', '1637-1645', '1647', '1654', '1657', '1662-1665', '1672-1674', '1689-1690']
@pytest.mark.parametrize(
    "this_state, tab, package, func_name, result_type, parameter_names, raises_ex, result, return_type",
    [
        (
            CoverageInfo(
                args=["all_types.get_item_at_index"],
                kwargs={},
                globals_before={},
                globals_after={},
                result="[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
                coverage=[
                    1040,
                    1042,
                    1043,
                    1044,
                    1045,
                    1046,
                    1048,
                    1049,
                    1050,
                    1051,
                    1063,
                    1064,
                    1066,
                    1069,
                    1072,
                    1082,
                    1084,
                    1086,
                    1087,
                    1088,
                    1089,
                    1090,
                    1091,
                    1092,
                    1096,
                    1097,
                    1098,
                    1099,
                    1100,
                    1101,
                    1103,
                    1107,
                    1112,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.005,
                result_type="list",
            ),
            "  ",
            "unit_test_generator",
            "return_function_line_numbers_and_accessed_globals",
            "list",
            ["f"],
            False,
            "['    x = unit_test_generator.return_function_line_numbers_and_accessed_globals(f)\\n', '    assert isinstance(x, return_type)\\n', '    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)\\n']",
            list,
        ),
    ],
)
def test_meta_program_function_call(
    this_state,
    tab,
    package,
    func_name,
    result_type,
    parameter_names,
    raises_ex,
    result,
    return_type,
):
    """
    Programmatically generated test function for meta_program_function_call
    """
    x = unit_test_generator.meta_program_function_call(
        this_state, tab, package, func_name, result_type, parameter_names, raises_ex
    )
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
