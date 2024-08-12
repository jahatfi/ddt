"""
Programmatically generated test function for auto_generate_tests()
"""

import re
import pytest
from src import unit_test_generator
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to auto_generate_tests:
from src.unit_test_generator import FunctionMetaData
from pprint import PrettyPrinter
from logging import PlaceHolder
from _io import TextIOWrapper
from collections import defaultdict
from collections import OrderedDict
from src.unit_test_generator import CoverageInfo
from logging import StreamHandler
from pathlib import WindowsPath
from logging import Logger
from logging import Manager
from logging import RootLogger

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
                "671a77a6d2b489034807d748e22a5173e37d9e6d57329eede1e7b6d412260843": CoverageInfo(
                    args_before=[
                        "<function append_list at 0x000002D2CF196B60>",
                        "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_metadata",
                                "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})",
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
                        1453,
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
            coverage_percentage=64.1,
            types_in_use={
                "logging.RootLogger",
                "logging.Manager",
                "pass_by_assignment.append_list",
                "logging.PlaceHolder",
                "src.unit_test_generator.FunctionMetaData",
                "pathlib.WindowsPath",
                "logging.StreamHandler",
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
                1453,
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
        "append_list": FunctionMetaData(
            name="append_list",
            parameter_names=["this_list", "item"],
            is_method=False,
            lines=[41, 42],
            non_code_lines=set(),
            global_vars_read_from={"logger"},
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py"
            ),
            coverage_io={
                "41d2d788826b24b7663c460d9fe9b99ae9d847486026e9c41dd367c5d37068cd": CoverageInfo(
                    args_before=["[1, 2, 3, 4]", "6"],
                    args_after=OrderedDict([("this_list", "[1, 2, 3, 4, 6]")]),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[41, 42],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            coverage_percentage=100.0,
            types_in_use={
                "logging.RootLogger",
                "logging.Manager",
                "logging.PlaceHolder",
                "logging.StreamHandler",
                "logging.Logger",
            },
            unified_test_coverage={41, 42},
            needs_pytest=False,
            callable_files={
                "append_list": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py"
            },
        ),
        "overwrite_list": FunctionMetaData(
            name="overwrite_list",
            parameter_names=["this_list"],
            is_method=False,
            lines=[51, 52],
            non_code_lines=set(),
            global_vars_read_from=set(),
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py"
            ),
            coverage_io={
                "3a457b3fa7a76eef0fefd90d54716eee8e40ce3dd5f99aff349b890e6bf7a440": CoverageInfo(
                    args_before=["[6, 4, 3, 2, 1]"],
                    args_after=OrderedDict([("this_list", "[6, 4, 3, 2, 1]")]),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[51, 52],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            coverage_percentage=100.0,
            types_in_use=set(),
            unified_test_coverage={51, 52},
            needs_pytest=False,
            callable_files={
                "overwrite_list": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py"
            },
        ),
        "increment_my_list_kwargs": FunctionMetaData(
            name="increment_my_list_kwargs",
            parameter_names=[],
            is_method=False,
            lines=[60, 61, 62, 60],
            non_code_lines=set(),
            global_vars_read_from=set(),
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py"
            ),
            coverage_io={
                "4e9bece720611f2a237c80e6c1d94d2684c84abfc6a5e9ef8b087fa8714f078d": CoverageInfo(
                    args_before=[],
                    args_after=OrderedDict(),
                    kwargs={"my_list": [0, 3]},
                    kwargs_after=OrderedDict(
                        [("my_list", "[0, 3, 1, ClassForTesting('test')]")]
                    ),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[60, 61, 62],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            coverage_percentage=75.0,
            types_in_use={"__main__.ClassForTesting"},
            unified_test_coverage={60, 61, 62},
            needs_pytest=False,
            callable_files={
                "increment_my_list_kwargs": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py"
            },
        ),
        "add_to_my_set_kwargs": FunctionMetaData(
            name="add_to_my_set_kwargs",
            parameter_names=[],
            is_method=False,
            lines=[70, 71, 70],
            non_code_lines=set(),
            global_vars_read_from=set(),
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py"
            ),
            coverage_io={
                "1b177cafdf940e50d12724a764cb0cc7f839f27de1ee0db42ea6c73ab23f1ac6": CoverageInfo(
                    args_before=[],
                    args_after=OrderedDict(),
                    kwargs={"my_set": {0, 2, 3}},
                    kwargs_after=OrderedDict([("my_set", "{0, 1, 2, 3}")]),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[70, 71],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            coverage_percentage=66.67,
            types_in_use=set(),
            unified_test_coverage={70, 71},
            needs_pytest=False,
            callable_files={
                "add_to_my_set_kwargs": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\pass_by_assignment\\pass_by_assignment.py"
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
                    "671a77a6d2b489034807d748e22a5173e37d9e6d57329eede1e7b6d412260843": CoverageInfo(
                        args_before=[
                            "<function append_list at 0x000002D2CF196B60>",
                            "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_metadata",
                                    "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})",
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
                            1453,
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
                coverage_percentage=64.1,
                types_in_use={
                    "logging.RootLogger",
                    "logging.Manager",
                    "src.unit_test_generator.FunctionMetaData",
                    "logging.StreamHandler",
                    "logging.Logger",
                    "pathlib.WindowsPath",
                    "logging.PlaceHolder",
                    "pass_by_assignment.append_list",
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
                    1453,
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
                "671a77a6d2b489034807d748e22a5173e37d9e6d57329eede1e7b6d412260843": CoverageInfo(
                    args_before=[
                        "<function append_list at 0x000002D2CF196B60>",
                        "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_metadata",
                                "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\pass_by_assignment\\\\pass_by_assignment.py'})",
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
                        1453,
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
                "function_metadata": "FunctionMetaData(name='update_metadata', parameter_names=['f', 'this_metadata'], is_method=False, lines=[1431, 1432, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1453, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1460, 1455, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1469], non_code_lines={1442, 1434, 1452, 1454}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'671a77a6d2b489034807d748e22a5173e37d9e6d57329eede1e7b6d412260843': CoverageInfo(args_before=['<function append_list at 0x000002D2CF196B60>',\"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after=OrderedDict([('this_metadata', \"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\pass_by_assignment\\\\\\\\pass_by_assignment.py'})\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1453, 1455, 1463, 1464, 1465, 1466, 1467, 1468], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=64.1, types_in_use={'logging.RootLogger', 'logging.Manager', 'src.unit_test_generator.FunctionMetaData', 'logging.StreamHandler', 'logging.Logger', 'pathlib.WindowsPath', 'logging.PlaceHolder', 'pass_by_assignment.append_list'}, unified_test_coverage={1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1453, 1455, 1463, 1464, 1465, 1466, 1467, 1468}, needs_pytest=False, callable_files={'update_metadata': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
                "state": "{'671a77a6d2b489034807d748e22a5173e37d9e6d57329eede1e7b6d412260843': CoverageInfo(args_before=['<function append_list at 0x000002D2CF196B60>',\"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})\"], args_after={'this_metadata': \"FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[41, 42], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\\\\\Users\\\\\\\\James\\\\\\\\Documents\\\\\\\\CyberResources\\\\\\\\ddt\\\\\\\\tests\\\\\\\\pass_by_assignment\\\\\\\\pass_by_assignment.py'})\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='None', expected_type='NoneType', coverage=[1431, 1433, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1443, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1453, 1455, 1463, 1464, 1465, 1466, 1467, 1468], exception_type='', exception_message='', constructor='', cost=0.0)}",
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
