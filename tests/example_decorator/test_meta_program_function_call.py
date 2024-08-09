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
# ['1792-1793', '1701-1702', '1709-1711', '1715-1718', '1721', '1727-1728', '1733-1741', '1743', '1750', '1753', '1758-1763', '1770-1772']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "[5]",
                    '"c"',
                    '"Before"',
                    "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                ],
                args_after={
                    "obj": "[5]",
                    "this_coverage_info": "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                },
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                expected_type="src.unit_test_generator.CoverageInfo",
                coverage=[1521, 1524, 1529, 1537, 1538, 1541],
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
                    1521,
                    1522,
                    1523,
                    1524,
                    1525,
                    1526,
                    1527,
                    1529,
                    1537,
                    1538,
                    1539,
                    1540,
                    1541,
                ],
                non_code_lines={1536, 1528, 1530, 1531, 1532, 1533, 1534, 1535},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "2023abec2aa37dfa72e00c40de1e4891cbb45ee936a838ad599accb88fd3275f": CoverageInfo(
                        args_before=[
                            "[5]",
                            '"c"',
                            '"Before"',
                            "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        ],
                        args_after=OrderedDict(
                            [
                                ("obj", "[5]"),
                                (
                                    "this_coverage_info",
                                    "CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                                ),
                            ]
                        ),
                        kwargs={},
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        expected_type="src.unit_test_generator.CoverageInfo",
                        coverage=[1521, 1524, 1529, 1537, 1538, 1541],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.001,
                    )
                },
                coverage_percentage=46.15,
                types_in_use={"logging.Logger", "src.unit_test_generator.CoverageInfo"},
                unified_test_coverage={1537, 1538, 1541, 1521, 1524, 1529},
                needs_pytest=False,
                callable_files={
                    "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_global(obj,this_global,phase,this_coverage_info)\\n', '    assert isinstance(result, expected_type)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert args_after[\"obj\"] == obj or obj == eval(args_after[\"obj\"])\\n', '    assert args_after[\"this_coverage_info\"] == this_coverage_info or this_coverage_info == eval(args_after[\"this_coverage_info\"])\\n']",
            list,
            {
                "this_state": "CoverageInfo(args_before=['[5]', '\"c\"', '\"Before\"', \"CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after={'obj': '[5]', 'this_coverage_info': \"CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"}, kwargs={}, globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1521, 1524, 1529, 1537, 1538, 1541], exception_type='', exception_message='', constructor='', cost=0.001)",
                "function_metadata": "FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1521, 1522, 1523, 1524, 1525, 1526, 1527, 1529, 1537, 1538, 1539, 1540, 1541], non_code_lines={1536, 1528, 1530, 1531, 1532, 1533, 1534, 1535}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'2023abec2aa37dfa72e00c40de1e4891cbb45ee936a838ad599accb88fd3275f': CoverageInfo(args_before=['[5]', '\"c\"', '\"Before\"', \"CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after=OrderedDict([('obj', '[5]'), ('this_coverage_info', \"CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\")]), kwargs={}, globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['2', '7'], args_after={}, kwargs={}, globals_before={'c': [5]}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1521, 1524, 1529, 1537, 1538, 1541], exception_type='', exception_message='', constructor='', cost=0.001)}, coverage_percentage=46.15, types_in_use={'logging.Logger', 'src.unit_test_generator.CoverageInfo'}, unified_test_coverage={1537, 1538, 1541, 1521, 1524, 1529}, needs_pytest=False, callable_files={'update_global': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
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
    assert args_after["this_state"] == this_state or this_state == eval(
        args_after["this_state"]
    )
    assert args_after[
        "function_metadata"
    ] == function_metadata or function_metadata == eval(args_after["function_metadata"])
