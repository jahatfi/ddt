"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 51.95% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1792', '1799', '1802', '1807-1812', '1819-1821', '1840-1841', '1844-1845', '1749-1750', '1759-1760', '1764-1767', '1770', '1776-1777', '1782-1790']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "<function append_list at 0x000001ABD2FAA5C0>",
                    "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                ],
                args_after={
                    "this_metadata": "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[31, 32], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})"
                },
                kwargs={},
                kwargs_after={},
                globals_before={},
                globals_after={},
                expected_result="None",
                expected_type="NoneType",
                coverage=[
                    1256,
                    1258,
                    1260,
                    1261,
                    1262,
                    1263,
                    1264,
                    1265,
                    1266,
                    1268,
                    1270,
                    1271,
                    1272,
                    1273,
                    1274,
                    1275,
                    1276,
                    1278,
                    1280,
                    1288,
                    1289,
                    1290,
                    1291,
                    1292,
                    1293,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.0,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_metadata",
                parameter_names=["f", "this_metadata"],
                is_method=False,
                lines=[
                    1256,
                    1257,
                    1258,
                    1260,
                    1261,
                    1262,
                    1263,
                    1264,
                    1265,
                    1266,
                    1268,
                    1269,
                    1270,
                    1271,
                    1272,
                    1273,
                    1274,
                    1275,
                    1276,
                    1278,
                    1280,
                    1281,
                    1282,
                    1283,
                    1284,
                    1285,
                    1286,
                    1287,
                    1285,
                    1280,
                    1288,
                    1289,
                    1290,
                    1291,
                    1292,
                    1293,
                    1294,
                    1295,
                    1294,
                ],
                non_code_lines={1279, 1259, 1277, 1267},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "d6282428a99b83c2f9715e23e190dd5b4ef77aed5e4a4dd2e23c077fbd931a4d": CoverageInfo(
                        args_before=[
                            "<function append_list at 0x000001ABD2FAA5C0>",
                            "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_metadata",
                                    "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[31, 32], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})",
                                )
                            ]
                        ),
                        kwargs={},
                        kwargs_after={},
                        globals_before={},
                        globals_after={},
                        expected_result="None",
                        expected_type="NoneType",
                        coverage=[
                            1256,
                            1258,
                            1260,
                            1261,
                            1262,
                            1263,
                            1264,
                            1265,
                            1266,
                            1268,
                            1270,
                            1271,
                            1272,
                            1273,
                            1274,
                            1275,
                            1276,
                            1278,
                            1280,
                            1288,
                            1289,
                            1290,
                            1291,
                            1292,
                            1293,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.0,
                    )
                },
                coverage_percentage=64.1,
                types_in_use={
                    "pass_by_assignment",
                    "pathlib.WindowsPath",
                    "src.unit_test_generator.FunctionMetaData",
                    "logging.Logger",
                },
                unified_test_coverage={
                    1280,
                    1288,
                    1289,
                    1290,
                    1291,
                    1292,
                    1293,
                    1256,
                    1258,
                    1260,
                    1261,
                    1262,
                    1263,
                    1264,
                    1265,
                    1266,
                    1268,
                    1270,
                    1271,
                    1272,
                    1273,
                    1274,
                    1275,
                    1276,
                    1278,
                },
                needs_pytest=False,
                callable_files={
                    "update_metadata": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_metadata(f,this_metadata)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_metadata == eval(args_after[\"this_metadata\"]) or args_after[\"this_metadata\"] == this_metadata\\n']",
            {
                "this_state": "CoverageInfo(args_before=['<function append_list at 0x000001ABD2FAA5C0>', \"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[31, 32], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\pass_by_assignment\\\\\\\\pass_by_assignment.py'})\"}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1256, 1258, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1268, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1278, 1280, 1288, 1289, 1290, 1291, 1292, 1293], exception_type='', exception_message='', constructor='', cost=0.0)",
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1256, 1257, 1258, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1278, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1285, 1280, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1294], non_code_lines={1279, 1259, 1277, 1267}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'d6282428a99b83c2f9715e23e190dd5b4ef77aed5e4a4dd2e23c077fbd931a4d': CoverageInfo(args_before=['<function append_list at 0x000001ABD2FAA5C0>', \"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[31, 32], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\pass_by_assignment\\\\\\\\pass_by_assignment.py'})\")]), kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1256, 1258, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1268, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1278, 1280, 1288, 1289, 1290, 1291, 1292, 1293], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=64.1, types_in_use={'pass_by_assignment', 'pathlib.WindowsPath', 'src.unit_test_generator.FunctionMetaData', 'logging.Logger'}, unified_test_coverage={1280, 1288, 1289, 1290, 1291, 1292, 1293, 1256, 1258, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1268, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1278}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
            },
        ),
    ],
)
def test_meta_program_function_call(
    this_state, tab, package, function_metadata, expected_result, args_after
):
    """
    Programmatically generated test function for meta_program_function_call()
    """
    result = unit_test_generator.meta_program_function_call(
        this_state, tab, package, function_metadata
    )
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_state == eval(args_after["this_state"])
        or args_after["this_state"] == this_state
    )
    assert (
        function_metadata == eval(args_after["function_metadata"])
        or args_after["function_metadata"] == function_metadata
    )
