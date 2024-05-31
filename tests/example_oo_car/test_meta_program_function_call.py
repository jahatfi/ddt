"""
Programmatically generated test function for meta_program_function_call
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 49.3% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1568', '1594-1595', '1602-1604', '1608-1610', '1613', '1618-1619', '1621', '1625', '1637-1645', '1647', '1654', '1657', '1662-1665', '1672-1674', '1689-1690']
@pytest.mark.parametrize(
    "this_state, tab, package, func_name, result_type, parameter_names, raises_ex, result, return_type",
    [
        (
            CoverageInfo(
                args=[
                    "0",
                    '"method_call_counter"',
                    '"Before"',
                    "CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0, result_type='')",
                ],
                kwargs={},
                globals_before={},
                globals_after={},
                result="CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, result='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0, result_type='')",
                coverage=[1411, 1414, 1418, 1427, 1428, 1432, 1434],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.002,
                result_type="src.unit_test_generator.CoverageInfo",
            ),
            "  ",
            "unit_test_generator",
            "update_global",
            "src.unit_test_generator.CoverageInfo",
            ["obj", "this_global", "phase", "this_coverage_info"],
            False,
            "['    x = unit_test_generator.update_global(obj,this_global,phase,this_coverage_info)\\n', '    assert isinstance(x, return_type)\\n', '    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)\\n']",
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
