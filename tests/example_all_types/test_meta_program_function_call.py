"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath


# In sum, these tests covered 51.95% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1793', '1800', '1803', '1808-1813', '1820-1822', '1841-1842', '1845-1846', '1750-1751', '1760-1761', '1765-1768', '1771', '1777-1778', '1783-1791']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "<function get_item_at_index at 0x0000017E33CA3CE0>",
                    "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                ],
                args_after={
                    "this_metadata": "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\example_all_types\\\\all_types.py'})"
                },
                kwargs={},
                kwargs_after={},
                globals_before={},
                globals_after={},
                expected_result="None",
                expected_type="NoneType",
                coverage=[
                    1257,
                    1259,
                    1261,
                    1262,
                    1263,
                    1264,
                    1265,
                    1266,
                    1267,
                    1269,
                    1271,
                    1272,
                    1273,
                    1274,
                    1275,
                    1276,
                    1277,
                    1281,
                    1289,
                    1290,
                    1291,
                    1292,
                    1293,
                    1294,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.005,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_metadata",
                parameter_names=["f", "this_metadata"],
                is_method=False,
                lines=[
                    1257,
                    1258,
                    1259,
                    1261,
                    1262,
                    1263,
                    1264,
                    1265,
                    1266,
                    1267,
                    1269,
                    1270,
                    1271,
                    1272,
                    1273,
                    1274,
                    1275,
                    1276,
                    1277,
                    1279,
                    1281,
                    1282,
                    1283,
                    1284,
                    1285,
                    1286,
                    1287,
                    1288,
                    1286,
                    1281,
                    1289,
                    1290,
                    1291,
                    1292,
                    1293,
                    1294,
                    1295,
                    1296,
                    1295,
                ],
                non_code_lines={1280, 1278, 1260, 1268},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "95af21bcce7f9421fa884e6e4afed49ff4e242440192e2003e9eaeacad5f5806": CoverageInfo(
                        args_before=[
                            "<function get_item_at_index at 0x0000017E33CA3CE0>",
                            "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_metadata",
                                    "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\example_all_types\\\\all_types.py'})",
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
                            1257,
                            1259,
                            1261,
                            1262,
                            1263,
                            1264,
                            1265,
                            1266,
                            1267,
                            1269,
                            1271,
                            1272,
                            1273,
                            1274,
                            1275,
                            1276,
                            1277,
                            1281,
                            1289,
                            1290,
                            1291,
                            1292,
                            1293,
                            1294,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.005,
                    )
                },
                coverage_percentage=61.54,
                types_in_use={
                    "all_types",
                    "logging.Logger",
                    "src.unit_test_generator.FunctionMetaData",
                    "pathlib.WindowsPath",
                },
                unified_test_coverage={
                    1281,
                    1289,
                    1290,
                    1291,
                    1292,
                    1293,
                    1294,
                    1257,
                    1259,
                    1261,
                    1262,
                    1263,
                    1264,
                    1265,
                    1266,
                    1267,
                    1269,
                    1271,
                    1272,
                    1273,
                    1274,
                    1275,
                    1276,
                    1277,
                },
                needs_pytest=False,
                callable_files={
                    "update_metadata": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_metadata(f,this_metadata)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_metadata == eval(args_after[\"this_metadata\"]) or args_after[\"this_metadata\"] == this_metadata\\n']",
            {
                "this_state": "CoverageInfo(args_before=['<function get_item_at_index at 0x0000017E33CA3CE0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\example_all_types\\\\\\\\all_types.py'})\"}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1257, 1259, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1269, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1281, 1289, 1290, 1291, 1292, 1293, 1294], exception_type='', exception_message='', constructor='', cost=0.005)",
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1257, 1258, 1259, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1279, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1286, 1281, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1295], non_code_lines={1280, 1278, 1260, 1268}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'95af21bcce7f9421fa884e6e4afed49ff4e242440192e2003e9eaeacad5f5806': CoverageInfo(args_before=['<function get_item_at_index at 0x0000017E33CA3CE0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\example_all_types\\\\\\\\all_types.py'})\")]), kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1257, 1259, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1269, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1281, 1289, 1290, 1291, 1292, 1293, 1294], exception_type='', exception_message='', constructor='', cost=0.005)}, coverage_percentage=61.54, types_in_use={'all_types', 'logging.Logger', 'src.unit_test_generator.FunctionMetaData', 'pathlib.WindowsPath'}, unified_test_coverage={1281, 1289, 1290, 1291, 1292, 1293, 1294, 1257, 1259, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1269, 1271, 1272, 1273, 1274, 1275, 1276, 1277}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
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
