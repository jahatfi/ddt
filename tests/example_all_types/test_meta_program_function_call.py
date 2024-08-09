"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 51.95% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1797-1798', '1706-1707', '1714-1716', '1720-1723', '1726', '1732-1733', '1738-1746', '1748', '1755', '1758', '1763-1768', '1775-1777']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "<function get_item_at_index at 0x00000250068D3D80>",
                    "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                ],
                args_after={
                    "this_metadata": "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\example_all_types\\\\all_types.py'})"
                },
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="None",
                expected_type="NoneType",
                coverage=[
                    1213,
                    1215,
                    1217,
                    1218,
                    1219,
                    1220,
                    1221,
                    1222,
                    1223,
                    1225,
                    1227,
                    1228,
                    1229,
                    1230,
                    1231,
                    1232,
                    1233,
                    1237,
                    1245,
                    1246,
                    1247,
                    1248,
                    1249,
                    1250,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.003,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_metadata",
                parameter_names=["f", "this_metadata"],
                is_method=False,
                lines=[
                    1213,
                    1214,
                    1215,
                    1217,
                    1218,
                    1219,
                    1220,
                    1221,
                    1222,
                    1223,
                    1225,
                    1226,
                    1227,
                    1228,
                    1229,
                    1230,
                    1231,
                    1232,
                    1233,
                    1235,
                    1237,
                    1238,
                    1239,
                    1240,
                    1241,
                    1242,
                    1243,
                    1244,
                    1242,
                    1237,
                    1245,
                    1246,
                    1247,
                    1248,
                    1249,
                    1250,
                    1251,
                    1252,
                    1251,
                ],
                non_code_lines={1216, 1234, 1236, 1224},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "56d02025db10ec7839c550be1deccf8199ae81cfce99fe2546fa7d02f7fbbcdc": CoverageInfo(
                        args_before=[
                            "<function get_item_at_index at 0x00000250068D3D80>",
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
                        globals_before={},
                        globals_after={},
                        expected_result="None",
                        expected_type="NoneType",
                        coverage=[
                            1213,
                            1215,
                            1217,
                            1218,
                            1219,
                            1220,
                            1221,
                            1222,
                            1223,
                            1225,
                            1227,
                            1228,
                            1229,
                            1230,
                            1231,
                            1232,
                            1233,
                            1237,
                            1245,
                            1246,
                            1247,
                            1248,
                            1249,
                            1250,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.003,
                    )
                },
                coverage_percentage=61.54,
                types_in_use={
                    "all_types",
                    "pathlib.WindowsPath",
                    "src.unit_test_generator.FunctionMetaData",
                    "logging.Logger",
                },
                unified_test_coverage={
                    1213,
                    1215,
                    1217,
                    1218,
                    1219,
                    1220,
                    1221,
                    1222,
                    1223,
                    1225,
                    1227,
                    1228,
                    1229,
                    1230,
                    1231,
                    1232,
                    1233,
                    1237,
                    1245,
                    1246,
                    1247,
                    1248,
                    1249,
                    1250,
                },
                needs_pytest=False,
                callable_files={
                    "update_metadata": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_metadata(f,this_metadata)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_metadata == eval(args_after[\"this_metadata\"]) or args_after[\"this_metadata\"] == this_metadata\\n']",
            list,
            {
                "this_state": "CoverageInfo(args_before=['<function get_item_at_index at 0x00000250068D3D80>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\example_all_types\\\\\\\\all_types.py'})\"}, kwargs={}, globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1213, 1215, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1225, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1237, 1245, 1246, 1247, 1248, 1249, 1250], exception_type='', exception_message='', constructor='', cost=0.003)",
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1213, 1214, 1215, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1235, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1242, 1237, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1251], non_code_lines={1216, 1234, 1236, 1224}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'56d02025db10ec7839c550be1deccf8199ae81cfce99fe2546fa7d02f7fbbcdc': CoverageInfo(args_before=['<function get_item_at_index at 0x00000250068D3D80>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\example_all_types\\\\\\\\all_types.py'})\")]), kwargs={}, globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1213, 1215, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1225, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1237, 1245, 1246, 1247, 1248, 1249, 1250], exception_type='', exception_message='', constructor='', cost=0.003)}, coverage_percentage=61.54, types_in_use={'all_types', 'pathlib.WindowsPath', 'src.unit_test_generator.FunctionMetaData', 'logging.Logger'}, unified_test_coverage={1213, 1215, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1225, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1237, 1245, 1246, 1247, 1248, 1249, 1250}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
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
