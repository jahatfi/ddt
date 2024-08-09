"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from pathlib import WindowsPath
from src.unit_test_generator import CoverageInfo
from src.unit_test_generator import FunctionMetaData


# In sum, these tests covered 53.25% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1797-1798', '1706-1707', '1714-1716', '1720-1723', '1726', '1732-1733', '1738-1746', '1748', '1755', '1758', '1763-1768', '1775-1777']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "0",
                    '"method_call_counter"',
                    '"Before"',
                    "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                ],
                args_after={
                    "this_coverage_info": "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)"
                },
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                expected_type="src.unit_test_generator.CoverageInfo",
                coverage=[1526, 1529, 1534, 1542, 1543, 1546],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.001,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_global",
                parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
                is_method=False,
                lines=[
                    1526,
                    1527,
                    1528,
                    1529,
                    1530,
                    1531,
                    1532,
                    1534,
                    1542,
                    1543,
                    1544,
                    1545,
                    1546,
                ],
                non_code_lines={1536, 1537, 1538, 1539, 1540, 1541, 1533, 1535},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "a90f49ace18951b10d8d03d3eef010fdbe52ad2589f6ea6551bf26dfe965e079": CoverageInfo(
                        args_before=[
                            "0",
                            '"method_call_counter"',
                            '"Before"',
                            "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_coverage_info",
                                    "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                                )
                            ]
                        ),
                        kwargs={},
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                        expected_type="src.unit_test_generator.CoverageInfo",
                        coverage=[1526, 1529, 1534, 1542, 1543, 1546],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.001,
                    )
                },
                coverage_percentage=46.15,
                types_in_use={"logging.Logger", "src.unit_test_generator.CoverageInfo"},
                unified_test_coverage={1542, 1543, 1546, 1526, 1529, 1534},
                needs_pytest=False,
                callable_files={
                    "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_global(obj,this_global,phase,this_coverage_info)\\n', '    assert isinstance(result, expected_type)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_coverage_info == eval(args_after[\"this_coverage_info\"]) or args_after[\"this_coverage_info\"] == this_coverage_info\\n']",
            list,
            {
                "this_state": "CoverageInfo(args_before=['0', '\"method_call_counter\"', '\"Before\"', 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)'], args_after={'this_coverage_info': 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)'}, kwargs={}, globals_before={}, globals_after={}, expected_result='CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)', expected_type='src.unit_test_generator.CoverageInfo', coverage=[1526, 1529, 1534, 1542, 1543, 1546], exception_type='', exception_message='', constructor='', cost=0.001)",
                "function_metadata": "FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1526, 1527, 1528, 1529, 1530, 1531, 1532, 1534, 1542, 1543, 1544, 1545, 1546], non_code_lines={1536, 1537, 1538, 1539, 1540, 1541, 1533, 1535}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'a90f49ace18951b10d8d03d3eef010fdbe52ad2589f6ea6551bf26dfe965e079': CoverageInfo(args_before=['0', '\"method_call_counter\"', '\"Before\"', 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)'], args_after=OrderedDict([('this_coverage_info', 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)')]), kwargs={}, globals_before={}, globals_after={}, expected_result='CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)', expected_type='src.unit_test_generator.CoverageInfo', coverage=[1526, 1529, 1534, 1542, 1543, 1546], exception_type='', exception_message='', constructor='', cost=0.001)}, coverage_percentage=46.15, types_in_use={'logging.Logger', 'src.unit_test_generator.CoverageInfo'}, unified_test_coverage={1542, 1543, 1546, 1526, 1529, 1534}, needs_pytest=False, callable_files={'update_global': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
            },
        ),
    ],
)
def test_meta_program_function_call(
    this_state,
    tab,
    package,
    function_metadata,
    expected_result,
    expected_type,
    args_after,
):
    """
    Programmatically generated test function for meta_program_function_call()
    """
    result = unit_test_generator.meta_program_function_call(
        this_state, tab, package, function_metadata
    )
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_state == eval(args_after["this_state"])
        or args_after["this_state"] == this_state
    )
    assert (
        function_metadata == eval(args_after["function_metadata"])
        or args_after["function_metadata"] == function_metadata
    )
