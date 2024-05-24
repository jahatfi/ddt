"""
Programmatically generated test function for meta_program_function_call
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 47.62% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1550', '1569-1573', '1578-1580', '1585-1590', '1594', '1600-1602', '1605', '1608-1611', '1616', '1619', '1624-1627', '1634-1635']
@pytest.mark.parametrize(
    "this_state,tab,package,func_name,result_type,parameter_names, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
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
                cost=0.004,
                result_type="list",
            ),
            "  ",
            "unit_test_generator",
            "return_function_line_numbers_and_accessed_globals",
            "list",
            ["f"],
            "N/A",
            "N/A",
            "N/A",
            "['  x = unit_test_generator.return_function_line_numbers_and_accessed_globals(f)\\n', '  assert x == result or repr(x) == result or repr(result) == x\\n']",
            "list",
            {},
            {},
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
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for meta_program_function_call
    """
    x = unit_test_generator.meta_program_function_call(
        this_state, tab, package, func_name, result_type, parameter_names
    )
    assert x == result or repr(x) == result or repr(result) == x
