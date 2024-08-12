"""
Programmatically generated test function for auto_generate_tests()
"""

import re
import pytest
from src import unit_test_generator
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to auto_generate_tests:
from logging import PlaceHolder
from pathlib import WindowsPath
from collections import OrderedDict
from collections import defaultdict
from _io import TextIOWrapper
from pprint import PrettyPrinter
from src.unit_test_generator import FunctionMetaData
from logging import Logger
from logging import StreamHandler
from logging import Manager
from src.unit_test_generator import CoverageInfo
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
            coverage_io={
                "8166805eeb92c68ad8ec5c0419539330d380bd3605464ef3e91d2dbb832dd0af": CoverageInfo(
                    args_before=[
                        "0",
                        '"error_code"',
                        '"Before"',
                        "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    expected_type="src.unit_test_generator.CoverageInfo",
                    coverage=[1607, 1610, 1615, 1623, 1624, 1627],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            coverage_percentage=46.15,
            types_in_use={
                "logging.StreamHandler",
                "logging.RootLogger",
                "logging.PlaceHolder",
                "logging.Logger",
                "logging.Manager",
                "src.unit_test_generator.CoverageInfo",
            },
            unified_test_coverage={1607, 1610, 1615, 1623, 1624, 1627},
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
                "3b7e03b8aae859800d2f91dcb379b509848e96b06e40032403fc9a05dddc38ce": CoverageInfo(
                    args_before=[
                        "<function divide_ints at 0x000001D91F8104A0>",
                        "FunctionMetaData(name='divide_ints', parameter_names=['a', 'b'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/procedural_division/divide_ints.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_metadata",
                                "FunctionMetaData(name='divide_ints', parameter_names=['a', 'b'], is_method=False, lines=[32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], non_code_lines=set(), global_vars_read_from={'logger', 'error_code'}, global_vars_written_to={'error_code'}, source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/procedural_division/divide_ints.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'divide_ints': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\procedural_division\\\\divide_ints.py'})",
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
                        1456,
                        1457,
                        1458,
                        1459,
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
                    cost=0.01,
                )
            },
            coverage_percentage=74.36,
            types_in_use={
                "logging.StreamHandler",
                "logging.RootLogger",
                "src.unit_test_generator.FunctionMetaData",
                "logging.PlaceHolder",
                "divide_ints.divide_ints",
                "pathlib.WindowsPath",
                "logging.Logger",
                "logging.Manager",
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
                1456,
                1457,
                1458,
                1459,
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
        "divide_ints": FunctionMetaData(
            name="divide_ints",
            parameter_names=["a", "b"],
            is_method=False,
            lines=[32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
            non_code_lines=set(),
            global_vars_read_from={"logger", "error_code"},
            global_vars_written_to={"error_code"},
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/procedural_division/divide_ints.py"
            ),
            coverage_io={
                "3c3651fe9bf9ccfdd1a1aff6a70f7ed10020457da35226255464b77c65d9b9f1": CoverageInfo(
                    args_before=["6", "2"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"error_code": 0},
                    globals_after={"error_code": 0},
                    expected_result="6/2=3.0",
                    expected_type="str",
                    coverage=[32, 33, 36, 39, 42],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                ),
                "8dcd244d9477f2f2ad357ec77e59f72415baec689cd405b8f6194849632f34bc": CoverageInfo(
                    args_before=["3", "0"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"error_code": 0},
                    globals_after={"error_code": -3},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[32, 33, 36, 39, 40, 41],
                    exception_type="<class 'ValueError'>",
                    exception_message="ValueError: Cannot divide by zero!",
                    constructor="",
                    cost=0.0,
                ),
                "07a742d4d53ae6bf7189b38410c8560979026474279353f659adda1c5bcd46a8": CoverageInfo(
                    args_before=['"10"', "2"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"error_code": 0},
                    globals_after={"error_code": -1},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[32, 33, 34, 35],
                    exception_type="<class 'TypeError'>",
                    exception_message="TypeError: Variable a='10' is not an int!",
                    constructor="",
                    cost=0.0,
                ),
                "2ab261f2cc5c9bd11e8c9817bea4afdfda42f0608bcff0ddd4521ae6d59cc6e8": CoverageInfo(
                    args_before=["8", "[]"],
                    args_after=OrderedDict([("b", "[]")]),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"error_code": 0},
                    globals_after={"error_code": -2},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[32, 33, 36, 37, 38],
                    exception_type="<class 'TypeError'>",
                    exception_message="TypeError: Variable b=[] is not an int!",
                    constructor="",
                    cost=0.0,
                ),
            },
            coverage_percentage=100.0,
            types_in_use={
                "logging.StreamHandler",
                "logging.RootLogger",
                "logging.PlaceHolder",
                "logging.Logger",
                "logging.Manager",
            },
            unified_test_coverage={32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42},
            needs_pytest=True,
            callable_files={
                "divide_ints": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\procedural_division\\divide_ints.py"
            },
        ),
    },
)


# In sum, these tests covered 50.62% of auto_generate_tests's lines
# Line(s) not covered by ANY of the tests below:
# ['2049-2057', '2059-2060', '2062', '2064-2065', '2067-2069', '2071', '2076', '2078', '2082', '2094-2095', '2099-2102', '2104', '2106', '2112-2118', '2129', '2133', '2135-2136', '2138-2143', '2145', '2147-2148', '2150-2152', '2155', '2157', '2162', '2164', '2166-2167', '2171-2173', '2177-2188', '2198', '2202', '2217', '2227-2228', '2230', '2235-2236', '2238-2239', '2259-2261', '2279-2280', '2282-2287', '1907', '1926-1931', '1933-1934', '1936-1937', '1947-1950', '1952-1957', '1959-1961', '1971-1972', '1985-1986', '1988', '2006', '2010-2011', '2013-2014', '2020-2021', '2023-2024', '2026-2027', '2034', '2037-2038']
@pytest.mark.parametrize(
    "function_metadata, state, function_name, source_file, tests_dir, outdir, indent_size, expected_result, args_after, globals_before",
    [
        (
            FunctionMetaData(
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
                coverage_io={
                    "8166805eeb92c68ad8ec5c0419539330d380bd3605464ef3e91d2dbb832dd0af": CoverageInfo(
                        args_before=[
                            "0",
                            '"error_code"',
                            '"Before"',
                            "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_coverage_info",
                                    "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                                )
                            ]
                        ),
                        kwargs={},
                        kwargs_after=OrderedDict(),
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        expected_type="src.unit_test_generator.CoverageInfo",
                        coverage=[1607, 1610, 1615, 1623, 1624, 1627],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.0,
                    )
                },
                coverage_percentage=46.15,
                types_in_use={
                    "logging.Logger",
                    "logging.StreamHandler",
                    "logging.RootLogger",
                    "logging.Manager",
                    "logging.PlaceHolder",
                    "src.unit_test_generator.CoverageInfo",
                },
                unified_test_coverage={1607, 1610, 1615, 1623, 1624, 1627},
                needs_pytest=False,
                callable_files={
                    "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            {
                "8166805eeb92c68ad8ec5c0419539330d380bd3605464ef3e91d2dbb832dd0af": CoverageInfo(
                    args_before=[
                        "0",
                        '"error_code"',
                        '"Before"',
                        "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    expected_type="src.unit_test_generator.CoverageInfo",
                    coverage=[1607, 1610, 1615, 1623, 1624, 1627],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            "update_global",
            WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
            ),
            WindowsPath("."),
            WindowsPath("."),
            2,
            "252acc6c11e8af0020608482027ff01a094facec4dddd6c5b97a134d630b6692",
            {
                "function_metadata": "FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1607, 1608, 1609, 1610, 1611, 1612, 1613, 1615, 1623, 1624, 1625, 1626, 1627], non_code_lines={1614, 1616, 1617, 1618, 1619, 1620, 1621, 1622}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'8166805eeb92c68ad8ec5c0419539330d380bd3605464ef3e91d2dbb832dd0af': CoverageInfo(args_before=['0','\"error_code\"','\"Before\"',\"CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after=OrderedDict([('this_coverage_info', \"CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1607, 1610, 1615, 1623, 1624, 1627], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=46.15, types_in_use={'logging.Logger', 'logging.StreamHandler', 'logging.RootLogger', 'logging.Manager', 'logging.PlaceHolder', 'src.unit_test_generator.CoverageInfo'}, unified_test_coverage={1607, 1610, 1615, 1623, 1624, 1627}, needs_pytest=False, callable_files={'update_global': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
                "state": "{'8166805eeb92c68ad8ec5c0419539330d380bd3605464ef3e91d2dbb832dd0af': CoverageInfo(args_before=['0','\"error_code\"','\"Before\"',\"CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after={'this_coverage_info': \"CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6','2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1607, 1610, 1615, 1623, 1624, 1627], exception_type='', exception_message='', constructor='', cost=0.0)}",
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
