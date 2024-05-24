"""
Programmatically generated test function for meta_program_function_call
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 44.44% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1550', '1569-1573', '1578-1580', '1585-1590', '1595-1596', '1598', '1600-1602', '1605', '1608-1611', '1616', '1619', '1624-1627', '1634-1635']
@pytest.mark.parametrize(
    "this_state,tab,package,func_name,result_type,parameter_names, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            CoverageInfo(
                args=[
                    "0",
                    '"error_code"',
                    '"Before"',
                    "CoverageInfo(args=['6', '2'], kwargs={}, globals_before={}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
                ],
                kwargs={},
                globals_before={},
                globals_after={},
                result="CoverageInfo(args=['6', '2'], kwargs={}, globals_before={'error_code': '0'}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0, result_type='')",
                coverage=[1401, 1404, 1408, 1412, 1413, 1416, 1442, 1444],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.001,
                result_type="src.unit_test_generator.CoverageInfo",
            ),
            "  ",
            "unit_test_generator",
            "update_global",
            "src.unit_test_generator.CoverageInfo",
            ["obj", "this_global", "phase", "this_coverage_info"],
            "N/A",
            "N/A",
            "N/A",
            "['  x = unit_test_generator.update_global(obj,this_global,phase,this_coverage_info)\\n', '  assert x == result or repr(x) == result or repr(result) == x\\n']",
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
