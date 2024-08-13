"""
Programmatically generated test function for meta_program_function_call()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo
from collections import OrderedDict
from logging import RootLogger
from pathlib import WindowsPath
from logging import StreamHandler
from logging import Logger
from logging import Manager
from src.unit_test_generator import FunctionMetaData
from logging import PlaceHolder


# In sum, these tests covered 51.95% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1797-1798', '1802-1805', '1808', '1814-1815', '1820-1828', '1830', '1837', '1840', '1845-1850', '1857-1859', '1878-1879', '1882-1883', '1787-1788']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    "<function get_item_at_index at 0x0000023B4B6B3EC0>",
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
                    1431,
                    1433,
                    1435,
                    1436,
                    1437,
                    1438,
                    1439,
                    1440,
                    1441,
                    1443,
                    1445,
                    1446,
                    1447,
                    1448,
                    1449,
                    1450,
                    1451,
                    1455,
                    1463,
                    1464,
                    1465,
                    1466,
                    1467,
                    1468,
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
                    1443,
                    1444,
                    1445,
                    1446,
                    1447,
                    1448,
                    1449,
                    1450,
                    1451,
                    1453,
                    1455,
                    1456,
                    1457,
                    1458,
                    1459,
                    1460,
                    1461,
                    1462,
                    1460,
                    1455,
                    1463,
                    1464,
                    1465,
                    1466,
                    1467,
                    1468,
                    1469,
                    1470,
                    1469,
                ],
                non_code_lines={1442, 1434, 1452, 1454},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "8f5cfd3e57255862d269f45e1bb9d6d357da6f25da786a4a87e87096773ca972": CoverageInfo(
                        args_before=[
                            "<function get_item_at_index at 0x0000023B4B6B3EC0>",
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
                            1431,
                            1433,
                            1435,
                            1436,
                            1437,
                            1438,
                            1439,
                            1440,
                            1441,
                            1443,
                            1445,
                            1446,
                            1447,
                            1448,
                            1449,
                            1450,
                            1451,
                            1455,
                            1463,
                            1464,
                            1465,
                            1466,
                            1467,
                            1468,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.0,
                    )
                },
                coverage_percentage=61.54,
                types_in_use={
                    "logging.StreamHandler",
                    "all_types.get_item_at_index",
                    "logging.Manager",
                    "logging.RootLogger",
                    "logging.PlaceHolder",
                    "pathlib.WindowsPath",
                    "src.unit_test_generator.FunctionMetaData",
                    "logging.Logger",
                },
                unified_test_coverage={
                    1431,
                    1433,
                    1435,
                    1436,
                    1437,
                    1438,
                    1439,
                    1440,
                    1441,
                    1443,
                    1445,
                    1446,
                    1447,
                    1448,
                    1449,
                    1450,
                    1451,
                    1455,
                    1463,
                    1464,
                    1465,
                    1466,
                    1467,
                    1468,
                },
                needs_pytest=False,
                callable_files={
                    "update_metadata": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_metadata(f,this_metadata)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_metadata == eval(args_after[\"this_metadata\"]) or args_after[\"this_metadata\"] == this_metadata\\n']",
            {
                "this_state": "CoverageInfo(args_before=['<function get_item_at_index at 0x0000023B4B6B3EC0>',\"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1455, 1463, 1464, 1465, 1466, 1467, 1468], exception_type='', exception_message='', constructor='', cost=0.0)",
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1431, 1432, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1453, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1460, 1455, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1469], non_code_lines={1442, 1434, 1452, 1454}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'8f5cfd3e57255862d269f45e1bb9d6d357da6f25da786a4a87e87096773ca972': CoverageInfo(args_before=['<function get_item_at_index at 0x0000023B4B6B3EC0>',\"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1455, 1463, 1464, 1465, 1466, 1467, 1468], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=61.54, types_in_use={'logging.StreamHandler', 'all_types.get_item_at_index', 'logging.Manager', 'logging.RootLogger', 'logging.PlaceHolder', 'pathlib.WindowsPath', 'src.unit_test_generator.FunctionMetaData', 'logging.Logger'}, unified_test_coverage={1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1455, 1463, 1464, 1465, 1466, 1467, 1468}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
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
