"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import FunctionMetaData
from src.unit_test_generator import CoverageInfo
from pathlib import WindowsPath


# In sum, these tests covered 51.95% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1794-1797', '1800', '1806-1807', '1812-1820', '1822', '1829', '1832', '1837-1842', '1849-1851', '1870-1871', '1874-1875', '1779-1780', '1789-1790']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "<function get_item_at_index at 0x000002209E6D3EC0>",
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
                    1423,
                    1425,
                    1427,
                    1428,
                    1429,
                    1430,
                    1431,
                    1432,
                    1433,
                    1435,
                    1437,
                    1438,
                    1439,
                    1440,
                    1441,
                    1442,
                    1443,
                    1447,
                    1455,
                    1456,
                    1457,
                    1458,
                    1459,
                    1460,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.01,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_metadata",
                parameter_names=["f", "this_metadata"],
                is_method=False,
                lines=[
                    1423,
                    1424,
                    1425,
                    1427,
                    1428,
                    1429,
                    1430,
                    1431,
                    1432,
                    1433,
                    1435,
                    1436,
                    1437,
                    1438,
                    1439,
                    1440,
                    1441,
                    1442,
                    1443,
                    1445,
                    1447,
                    1448,
                    1449,
                    1450,
                    1451,
                    1452,
                    1453,
                    1454,
                    1452,
                    1447,
                    1455,
                    1456,
                    1457,
                    1458,
                    1459,
                    1460,
                    1461,
                    1462,
                    1461,
                ],
                non_code_lines={1426, 1444, 1446, 1434},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "c21752efd74e0e16d987dc6d688293e087e9b12575c372ad01f058674370b402": CoverageInfo(
                        args_before=[
                            "<function get_item_at_index at 0x000002209E6D3EC0>",
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
                            1423,
                            1425,
                            1427,
                            1428,
                            1429,
                            1430,
                            1431,
                            1432,
                            1433,
                            1435,
                            1437,
                            1438,
                            1439,
                            1440,
                            1441,
                            1442,
                            1443,
                            1447,
                            1455,
                            1456,
                            1457,
                            1458,
                            1459,
                            1460,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.01,
                    )
                },
                coverage_percentage=61.54,
                types_in_use={
                    "src.unit_test_generator.FunctionMetaData",
                    "pathlib.WindowsPath",
                    "logging.Logger",
                    "logging.Manager",
                    "all_types.get_item_at_index",
                    "logging.StreamHandler",
                    "logging.RootLogger",
                    "logging.PlaceHolder",
                },
                unified_test_coverage={
                    1423,
                    1425,
                    1427,
                    1428,
                    1429,
                    1430,
                    1431,
                    1432,
                    1433,
                    1435,
                    1437,
                    1438,
                    1439,
                    1440,
                    1441,
                    1442,
                    1443,
                    1447,
                    1455,
                    1456,
                    1457,
                    1458,
                    1459,
                    1460,
                },
                needs_pytest=False,
                callable_files={
                    "update_metadata": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_metadata(f,this_metadata)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_metadata == eval(args_after[\"this_metadata\"]) or args_after[\"this_metadata\"] == this_metadata\\n']",
            {
                "this_state": "CoverageInfo(args_before=['<function get_item_at_index at 0x000002209E6D3EC0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1423, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1447, 1455, 1456, 1457, 1458, 1459, 1460], exception_type='', exception_message='', constructor='', cost=0.01)",
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1423, 1424, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1445, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1452, 1447, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1461], non_code_lines={1426, 1444, 1446, 1434}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'c21752efd74e0e16d987dc6d688293e087e9b12575c372ad01f058674370b402': CoverageInfo(args_before=['<function get_item_at_index at 0x000002209E6D3EC0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1423, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1447, 1455, 1456, 1457, 1458, 1459, 1460], exception_type='', exception_message='', constructor='', cost=0.01)}, coverage_percentage=61.54, types_in_use={'src.unit_test_generator.FunctionMetaData', 'pathlib.WindowsPath', 'logging.Logger', 'logging.Manager', 'all_types.get_item_at_index', 'logging.StreamHandler', 'logging.RootLogger', 'logging.PlaceHolder'}, unified_test_coverage={1423, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1447, 1455, 1456, 1457, 1458, 1459, 1460}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
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
