"""
Programmatically generated test function for auto_generate_tests()
"""

import re
import pytest
from src import unit_test_generator
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to auto_generate_tests:
from src.unit_test_generator import CoverageInfo
from collections import OrderedDict
from logging import RootLogger
from collections import defaultdict
from pathlib import WindowsPath
from logging import Logger
from logging import StreamHandler
from pprint import PrettyPrinter
from logging import Manager
from _io import TextIOWrapper
from src.unit_test_generator import FunctionMetaData
from logging import PlaceHolder

ALL_METADATA = defaultdict(
    FunctionMetaData,
    {
        "update_global": FunctionMetaData(
            name="update_global",
            parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
            is_method=False,
            lines=[
                1607,
                1608,
                1609,
                1610,
                1611,
                1612,
                1613,
                1615,
                1623,
                1624,
                1625,
                1626,
                1627,
            ],
            non_code_lines={1614, 1616, 1617, 1618, 1619, 1620, 1621, 1622},
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
            non_code_lines={1442, 1452, 1454, 1434},
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
                "all_types.get_item_at_index",
                "logging.Manager",
                "logging.RootLogger",
                "src.unit_test_generator.FunctionMetaData",
                "logging.Logger",
                "logging.StreamHandler",
                "pathlib.WindowsPath",
                "logging.PlaceHolder",
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


# In sum, these tests covered 52.81% of auto_generate_tests's lines
# Line(s) not covered by ANY of the tests below:
# ['2049-2057', '2059-2060', '2062', '2064-2065', '2067-2069', '2071', '2076', '2078', '2082', '2094-2095', '2099-2102', '2104', '2106', '2129', '2133', '2135-2136', '2138-2143', '2145', '2147-2148', '2150-2152', '2155', '2157', '2162', '2164', '2166-2167', '2171-2173', '2177-2188', '2198', '2202', '2217', '2227-2228', '2230', '2235-2236', '2238-2239', '2259-2261', '2279-2280', '2282-2287', '1907', '1926-1931', '1933-1934', '1936-1937', '1947-1950', '1952-1957', '1959-1961', '1971-1972', '1985-1986', '1988', '2006', '2010-2011', '2013-2014', '2020-2021', '2023-2024', '2026-2027', '2034', '2037-2038']
@pytest.mark.parametrize(
    "function_metadata, state, function_name, source_file, tests_dir, outdir, indent_size, expected_result, args_after, globals_before",
    [
        (
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
            {
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
            "update_metadata",
            WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
            ),
            WindowsPath("."),
            WindowsPath("."),
            2,
            "1fbe0a44c2a782f985566cccd21c7b422d52ddd333521a966c82de2c70f8c2d1",
            {
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1431, 1432, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1453, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1460, 1455, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1469], non_code_lines={1442, 1434, 1452, 1454}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'8f5cfd3e57255862d269f45e1bb9d6d357da6f25da786a4a87e87096773ca972': CoverageInfo(args_before=['<function get_item_at_index at 0x0000023B4B6B3EC0>',\"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1455, 1463, 1464, 1465, 1466, 1467, 1468], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=61.54, types_in_use={'logging.StreamHandler', 'all_types.get_item_at_index', 'logging.Manager', 'logging.RootLogger', 'logging.PlaceHolder', 'pathlib.WindowsPath', 'src.unit_test_generator.FunctionMetaData', 'logging.Logger'}, unified_test_coverage={1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1455, 1463, 1464, 1465, 1466, 1467, 1468}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
                "state": "{'8f5cfd3e57255862d269f45e1bb9d6d357da6f25da786a4a87e87096773ca972': CoverageInfo(args_before=['<function get_item_at_index at 0x0000023B4B6B3EC0>',\"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[29, 30, 31, 32, 33, 34, 36], non_code_lines={35}, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'get_item_at_index': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\all_types\\\\\\\\all_types.py'})\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1455, 1463, 1464, 1465, 1466, 1467, 1468], exception_type='', exception_message='', constructor='', cost=0.0)}",
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
