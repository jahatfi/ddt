"""
Programmatically generated test function for meta_program_function_call()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData
from logging import Logger
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 51.95% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1793-1794', '1799-1807', '1809', '1816', '1819', '1824-1829', '1836-1838', '1857-1858', '1861-1862', '1766-1767', '1776-1777', '1781-1784']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "<function get_item_at_index at 0x0000026CE9EA3EC0>",
                    "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                ],
                args_after={
                    "this_metadata": "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\all_types\\\\all_types.py'})"
                },
                kwargs={},
                kwargs_after=OrderedDict(),
                globals_before={},
                globals_after={},
                expected_result="None",
                expected_type="NoneType",
                coverage=[
                    1411,
                    1413,
                    1415,
                    1416,
                    1417,
                    1418,
                    1419,
                    1420,
                    1421,
                    1423,
                    1425,
                    1426,
                    1427,
                    1428,
                    1429,
                    1430,
                    1431,
                    1435,
                    1443,
                    1444,
                    1445,
                    1446,
                    1447,
                    1448,
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
                    1411,
                    1412,
                    1413,
                    1415,
                    1416,
                    1417,
                    1418,
                    1419,
                    1420,
                    1421,
                    1423,
                    1424,
                    1425,
                    1426,
                    1427,
                    1428,
                    1429,
                    1430,
                    1431,
                    1433,
                    1435,
                    1436,
                    1437,
                    1438,
                    1439,
                    1440,
                    1441,
                    1442,
                    1440,
                    1435,
                    1443,
                    1444,
                    1445,
                    1446,
                    1447,
                    1448,
                    1449,
                    1450,
                    1449,
                ],
                non_code_lines={1432, 1434, 1422, 1414},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "f4390f2315caf03deded8c425c539f61940fd46667c0d7a61842bc02675b7812": CoverageInfo(
                        args_before=[
                            "<function get_item_at_index at 0x0000026CE9EA3EC0>",
                            "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_metadata",
                                    "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\all_types\\\\all_types.py'})",
                                )
                            ]
                        ),
                        kwargs={},
                        kwargs_after=OrderedDict(),
                        globals_before={},
                        globals_after={},
                        expected_result="None",
                        expected_type="NoneType",
                        coverage=[
                            1411,
                            1413,
                            1415,
                            1416,
                            1417,
                            1418,
                            1419,
                            1420,
                            1421,
                            1423,
                            1425,
                            1426,
                            1427,
                            1428,
                            1429,
                            1430,
                            1431,
                            1435,
                            1443,
                            1444,
                            1445,
                            1446,
                            1447,
                            1448,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.0,
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
                    1411,
                    1413,
                    1415,
                    1416,
                    1417,
                    1418,
                    1419,
                    1420,
                    1421,
                    1423,
                    1425,
                    1426,
                    1427,
                    1428,
                    1429,
                    1430,
                    1431,
                    1435,
                    1443,
                    1444,
                    1445,
                    1446,
                    1447,
                    1448,
                },
                needs_pytest=False,
                callable_files={
                    "update_metadata": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_metadata(f,this_metadata)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_metadata == eval(args_after[\"this_metadata\"]) or args_after[\"this_metadata\"] == this_metadata\\n']",
            {
                "this_state": "CoverageInfo(args_before=['<function get_item_at_index at 0x0000026CE9EA3EC0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1435, 1443, 1444, 1445, 1446, 1447, 1448], exception_type='', exception_message='', constructor='', cost=0.0)",
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1411, 1412, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1440, 1435, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1449], non_code_lines={1432, 1434, 1422, 1414}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'f4390f2315caf03deded8c425c539f61940fd46667c0d7a61842bc02675b7812': CoverageInfo(args_before=['<function get_item_at_index at 0x0000026CE9EA3EC0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1435, 1443, 1444, 1445, 1446, 1447, 1448], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=61.54, types_in_use={'all_types', 'logging.Logger', 'src.unit_test_generator.FunctionMetaData', 'pathlib.WindowsPath'}, unified_test_coverage={1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1435, 1443, 1444, 1445, 1446, 1447, 1448}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
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
