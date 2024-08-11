"""
Programmatically generated test function for auto_generate_tests()
"""
import re
import pytest
from src import unit_test_generator
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to auto_generate_tests:
from logging import Logger
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData
from pprint import PrettyPrinter
from collections import defaultdict
from src.unit_test_generator import CoverageInfo
ALL_METADATA = defaultdict(<class 'src.unit_test_generator.FunctionMetaData'>, {'update_global': FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1586, 1587, 1588, 1589, 1590, 1591, 1592, 1594, 1602, 1603, 1604, 1605, 1606], non_code_lines={1600, 1601, 1593, 1595, 1596, 1597, 1598, 1599}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'update_global': 'C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py'}), 'update_metadata': FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1411, 1412, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1440, 1435, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1449], non_code_lines={1432, 1434, 1422, 1414}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'9b86a932974766a3525f3f3a4a6c96d634bffa34cf40cd336b30be687f144e0b': CoverageInfo(args_before=['<function append_list at 0x0000014FFFEC6B60>', "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})"], args_after=OrderedDict([('this_metadata', "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=64.1, types_in_use={'logging.Logger', 'pass_by_assignment', 'src.unit_test_generator.FunctionMetaData', 'pathlib.WindowsPath'}, unified_test_coverage={1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448}, needs_pytest=False, callable_files={'update_metadata': 'C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py'}), 'append_list': FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={'41d2d788826b24b7663c460d9fe9b99ae9d847486026e9c41dd367c5d37068cd': CoverageInfo(args_before=['[1, 2, 3, 4]', '6'], args_after=OrderedDict([('this_list', '[1, 2, 3, 4, 6]')]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[41, 42], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=100.0, types_in_use={'logging.Logger'}, unified_test_coverage={41, 42}, needs_pytest=False, callable_files={'append_list': 'C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py'}), 'overwrite_list': FunctionMetaData(name='overwrite_list', parameter_names=['this_list'], is_method=False, lines=[51, 52], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={'3a457b3fa7a76eef0fefd90d54716eee8e40ce3dd5f99aff349b890e6bf7a440': CoverageInfo(args_before=['[6, 4, 3, 2, 1]'], args_after=OrderedDict([('this_list', '[6, 4, 3, 2, 1]')]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[51, 52], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=100.0, types_in_use=set(), unified_test_coverage={51, 52}, needs_pytest=False, callable_files={'overwrite_list': 'C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py'}), 'increment_my_list_kwargs': FunctionMetaData(name='increment_my_list_kwargs', parameter_names=[], is_method=False, lines=[60, 61, 62, 60], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={'4e9bece720611f2a237c80e6c1d94d2684c84abfc6a5e9ef8b087fa8714f078d': CoverageInfo(args_before=[], args_after=OrderedDict(), kwargs={'my_list': [0, 3]}, kwargs_after=OrderedDict([('my_list', "[0, 3, 1, ClassForTesting('test')]")]), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[60, 61, 62], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=75.0, types_in_use={'pass_by_assignment.ClassForTesting', '__main__.ClassForTesting'}, unified_test_coverage={60, 61, 62}, needs_pytest=False, callable_files={'increment_my_list_kwargs': 'C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py'}), 'add_to_my_set_kwargs': FunctionMetaData(name='add_to_my_set_kwargs', parameter_names=[], is_method=False, lines=[70, 71, 70], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={'1b177cafdf940e50d12724a764cb0cc7f839f27de1ee0db42ea6c73ab23f1ac6': CoverageInfo(args_before=[], args_after=OrderedDict(), kwargs={'my_set': {0, 2, 3}}, kwargs_after=OrderedDict([('my_set', '{0, 1, 2, 3}')]), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[70, 71], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=66.67, types_in_use=set(), unified_test_coverage={70, 71}, needs_pytest=False, callable_files={'add_to_my_set_kwargs': 'C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py'})})
  # In sum, these tests covered 54.17% of auto_generate_tests's lines
  # Line(s) not covered by ANY of the tests below:
  # ['2048', '2052', '2064-2065', '2069-2072', '2074', '2076', '2099', '2103', '2105-2106', '2108-2113', '2115', '2117-2118', '2120-2122', '2125', '2127', '2132', '2134', '2136-2137', '2141-2143', '2147-2158', '2168', '2172', '2187', '2197-2198', '2200', '2205-2206', '2208-2209', '2229-2231', '2249-2250', '2252-2257', '1886', '1905-1910', '1912-1913', '1915-1916', '1926-1929', '1931', '1941-1942', '1955-1956', '1958', '1976', '1980-1981', '1983-1984', '1990-1991', '1993-1994', '1996-1997', '2004', '2007-2008', '2015', '2019-2027', '2029-2030', '2032', '2034-2035', '2037-2039', '2041']
@pytest.mark.parametrize(
"function_metadata, state, function_name, source_file, tests_dir, outdir, indent_size, expected_result, args_after, globals_before",
[(FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1411, 1412, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1440, 1435, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1449], non_code_lines={1432, 1434, 1422, 1414}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'9b86a932974766a3525f3f3a4a6c96d634bffa34cf40cd336b30be687f144e0b': CoverageInfo(args_before=['<function append_list at 0x0000014FFFEC6B60>', "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})"], args_after=OrderedDict([('this_metadata', "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=64.1, types_in_use={'logging.Logger', 'pass_by_assignment', 'src.unit_test_generator.FunctionMetaData', 'pathlib.WindowsPath'}, unified_test_coverage={1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448}, needs_pytest=False, callable_files={'update_metadata': 'C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py'}),{'9b86a932974766a3525f3f3a4a6c96d634bffa34cf40cd336b30be687f144e0b': CoverageInfo(args_before=['<function append_list at 0x0000014FFFEC6B60>', "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})"], args_after=OrderedDict([('this_metadata', "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448], exception_type='', exception_message='', constructor='', cost=0.0)},"update_metadata",WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'),WindowsPath('.'),WindowsPath('.'),'1fbe0a44c2a782f985566cccd21c7b422d52ddd333521a966c82de2c70f8c2d1',{'function_metadata': 'FunctionMetaData(name=\'update_metadata\', parameter_names=[\'f\', \'this_metadata\'], is_method=False, lines=[1411, 1412, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1440, 1435, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1449], non_code_lines={1432, 1434, 1422, 1414}, global_vars_read_from={\'logger\'}, global_vars_written_to=set(), source_file=WindowsPath(\'C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py\'), coverage_io={\'9b86a932974766a3525f3f3a4a6c96d634bffa34cf40cd336b30be687f144e0b\': CoverageInfo(args_before=[\'<function append_list at 0x0000014FFFEC6B60>\', "FunctionMetaData(name=\'append_list\', parameter_names=[\'this_list\', \'item\'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath(\'C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py\'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})"], args_after=OrderedDict([(\'this_metadata\', "FunctionMetaData(name=\'append_list\', parameter_names=[\'this_list\', \'item\'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={\'logger\'}, global_vars_written_to=set(), source_file=WindowsPath(\'C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py\'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={\'append_list\': \'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\pass_by_assignment\\\\\\\\pass_by_assignment.py\'})")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\'None\', expected_type=\'NoneType\', coverage=[1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448], exception_type=\'\', exception_message=\'\', constructor=\'\', cost=0.0)}, coverage_percentage=64.1, types_in_use={\'logging.Logger\', \'pass_by_assignment\', \'src.unit_test_generator.FunctionMetaData\', \'pathlib.WindowsPath\'}, unified_test_coverage={1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448}, needs_pytest=False, callable_files={\'update_metadata\': \'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py\'})', 'state': '{\'9b86a932974766a3525f3f3a4a6c96d634bffa34cf40cd336b30be687f144e0b\': CoverageInfo(args_before=[\'<function append_list at 0x0000014FFFEC6B60>\', "FunctionMetaData(name=\'append_list\', parameter_names=[\'this_list\', \'item\'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath(\'C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py\'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})"], args_after={\'this_metadata\': "FunctionMetaData(name=\'append_list\', parameter_names=[\'this_list\', \'item\'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={\'logger\'}, global_vars_written_to=set(), source_file=WindowsPath(\'C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py\'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={\'append_list\': \'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\pass_by_assignment\\\\\\\\pass_by_assignment.py\'})"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\'None\', expected_type=\'NoneType\', coverage=[1411, 1413, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1423, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1435, 1443, 1444, 1445, 1446, 1447, 1448], exception_type=\'\', exception_message=\'\', constructor=\'\', cost=0.0)}', 'source_file': "WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py')", 'tests_dir': "WindowsPath('.')", 'outdir': "WindowsPath('.')"},{}),
])
def test_auto_generate_tests(function_metadata, state, function_name, source_file, tests_dir, outdir, indent_size, expected_result, args_after, globals_before):
    """
    Programmatically generated test function for auto_generate_tests()
    """
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr(unit_test_generator, "all_metadata", ALL_METADATA)
    result = unit_test_generator.auto_generate_tests(function_metadata,state,function_name,source_file,tests_dir,outdir,indent_size)
    assert result == expected_result or result == eval(expected_result)
    assert function_metadata == eval(args_after["function_metadata"]) or args_after["function_metadata"] == function_metadata
    assert state == eval(args_after["state"]) or args_after["state"] == state
    assert source_file == eval(args_after["source_file"]) or args_after["source_file"] == source_file
    assert tests_dir == eval(args_after["tests_dir"]) or args_after["tests_dir"] == tests_dir
    assert outdir == eval(args_after["outdir"]) or args_after["outdir"] == outdir
