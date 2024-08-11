"""
Programmatically generated test function for auto_generate_tests()
"""

import pytest
from src import unit_test_generator
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to auto_generate_tests:
from collections import defaultdict
from src.unit_test_generator import FunctionMetaData
from collections import OrderedDict
from src.unit_test_generator import CoverageInfo
from pathlib import WindowsPath

ALL_METADATA = defaultdict(
    FunctionMetaData,
    {
        "update_global": FunctionMetaData(
            name="update_global",
            parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
            is_method=False,
            lines=[
                1599,
                1600,
                1601,
                1602,
                1603,
                1604,
                1605,
                1607,
                1615,
                1616,
                1617,
                1618,
                1619,
            ],
            non_code_lines={1606, 1608, 1609, 1610, 1611, 1612, 1613, 1614},
            global_vars_read_from={"logger"},
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
            ),
            coverage_io={},
            coverage_percentage=0.0,
            types_in_use=set(),
            unified_test_coverage=set(),
            needs_pytest=False,
            callable_files={
                "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
            },
        ),
        "update_metadata": FunctionMetaData(
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
                "all_types.get_item_at_index",
                "logging.RootLogger",
                "pathlib.WindowsPath",
                "logging.Logger",
                "logging.Manager",
                "logging.StreamHandler",
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
        "get_item_at_index": FunctionMetaData(
            name="get_item_at_index",
            parameter_names=["iterable", "index"],
            is_method=False,
            lines=[29, 30, 31, 32, 33, 34, 36],
            non_code_lines={35},
            global_vars_read_from=set(),
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py"
            ),
            coverage_io={
                "1edeba54a64658dddb0ff23a35c06b12b5a92ff815a4fa728a18b112ca3f5a8a": CoverageInfo(
                    args_before=[
                        '"The quick red fox jumped over the lazy brown dog"',
                        "3",
                    ],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result=" ",
                    expected_type="str",
                    coverage=[29, 31, 33, 36],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                ),
                "5ac62d59657bfac04cf3ce48377adb129cadd4a9805d0ac28817844589527dd0": CoverageInfo(
                    args_before=["(5, 6, 7, 8, 9, 10, 11, 12, 13, 14)", "50"],
                    args_after=OrderedDict(
                        [("iterable", "(5, 6, 7, 8, 9, 10, 11, 12, 13, 14)")]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[29, 31, 32],
                    exception_type="<class 'ValueError'>",
                    exception_message="index must be in range [0, 9], was 50",
                    constructor="",
                    cost=0.0,
                ),
                "6ada6749e00170edea0441df3c3aaa576d3c3ccd15b95326f404c2c08c0cfb9a": CoverageInfo(
                    args_before=["[-1, -2, -3, -4]", "0"],
                    args_after=OrderedDict([("iterable", "[-1, -2, -3, -4]")]),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="-1",
                    expected_type="int",
                    coverage=[29, 31, 33, 36],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                ),
                "4af9da0fec2cbcc1502be3a9e1783eac06314de8c4435addbe985665e569908d": CoverageInfo(
                    args_before=['"a test string"', "-5"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[29, 31, 33, 34],
                    exception_type="<class 'ValueError'>",
                    exception_message="index must be in range [0, 12], was -5",
                    constructor="",
                    cost=0.0,
                ),
            },
            coverage_percentage=85.71,
            types_in_use=set(),
            unified_test_coverage={32, 33, 34, 36, 29, 31},
            needs_pytest=True,
            callable_files={
                "get_item_at_index": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\all_types\\all_types.py"
            },
        ),
    },
)


# In sum, these tests covered 51.51% of auto_generate_tests's lines
# Line(s) not covered by ANY of the tests below:
# ['2048-2049', '2051-2052', '2054', '2056-2057', '2059-2061', '2063', '2068', '2070', '2074', '2086-2087', '2091-2094', '2096', '2098', '2121', '2125', '2127-2128', '2130-2135', '2137', '2139-2140', '2142-2144', '2147', '2149', '2154', '2156', '2158-2159', '2163-2165', '2169-2180', '2190', '2194', '2209', '2219-2220', '2222', '2227-2228', '2230-2231', '2251-2253', '2271-2272', '2274-2279', '2285-2286', '2288-2293', '1899', '1918-1923', '1925-1926', '1928-1929', '1939-1942', '1944-1949', '1951-1953', '1963-1964', '1977-1978', '1980', '1998', '2002-2003', '2005-2006', '2012-2013', '2015-2016', '2018-2019', '2026', '2029-2030', '2037', '2041-2047']
@pytest.mark.parametrize(
    "function_metadata, state, function_name, source_file, tests_dir, outdir, indent_size, expected_result, args_after, globals_before",
    [
        (
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
            {
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
            "update_metadata",
            WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
            ),
            WindowsPath("."),
            WindowsPath("."),
            2,
            "1fbe0a44c2a782f985566cccd21c7b422d52ddd333521a966c82de2c70f8c2d1",
            {
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1423, 1424, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1445, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1452, 1447, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1461], non_code_lines={1426, 1444, 1446, 1434}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'c21752efd74e0e16d987dc6d688293e087e9b12575c372ad01f058674370b402': CoverageInfo(args_before=['<function get_item_at_index at 0x000002209E6D3EC0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1423, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1447, 1455, 1456, 1457, 1458, 1459, 1460], exception_type='', exception_message='', constructor='', cost=0.01)}, coverage_percentage=61.54, types_in_use={'src.unit_test_generator.FunctionMetaData', 'pathlib.WindowsPath', 'logging.Logger', 'logging.Manager', 'all_types.get_item_at_index', 'logging.StreamHandler', 'logging.RootLogger', 'logging.PlaceHolder'}, unified_test_coverage={1423, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1447, 1455, 1456, 1457, 1458, 1459, 1460}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
                "state": "{'c21752efd74e0e16d987dc6d688293e087e9b12575c372ad01f058674370b402': CoverageInfo(args_before=['<function get_item_at_index at 0x000002209E6D3EC0>', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1423, 1425, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1435, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1447, 1455, 1456, 1457, 1458, 1459, 1460], exception_type='', exception_message='', constructor='', cost=0.01)}",
                "source_file": "WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py')",
                "tests_dir": "WindowsPath('.')",
                "outdir": "WindowsPath('.')",
            },
            {},
        ),
    ],
)
def test_auto_generate_tests(
    function_metadata,
    state,
    function_name,
    source_file,
    tests_dir,
    outdir,
    indent_size,
    expected_result,
    args_after,
    globals_before,
):
    """
    Programmatically generated test function for auto_generate_tests()
    """
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr(unit_test_generator, "all_metadata", ALL_METADATA)
    result = unit_test_generator.auto_generate_tests(
        function_metadata,
        state,
        function_name,
        source_file,
        tests_dir,
        outdir,
        indent_size,
    )
    assert result == expected_result or result == eval(expected_result)
    assert (
        function_metadata == eval(args_after["function_metadata"])
        or args_after["function_metadata"] == function_metadata
    )
    assert state == eval(args_after["state"]) or args_after["state"] == state
    assert (
        source_file == eval(args_after["source_file"])
        or args_after["source_file"] == source_file
    )
    assert (
        tests_dir == eval(args_after["tests_dir"])
        or args_after["tests_dir"] == tests_dir
    )
    assert outdir == eval(args_after["outdir"]) or args_after["outdir"] == outdir
