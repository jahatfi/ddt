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
from src.unit_test_generator import CoverageInfo
from collections import defaultdict
from logging import Logger
from logging import StreamHandler
from _io import TextIOWrapper
from logging import RootLogger
from logging import Manager
from pathlib import WindowsPath
from logging import PlaceHolder
from collections import OrderedDict

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
                "364dbab6e996d2b07a239c6ce2e2df688159375398cc8e1cb47de9677b4e0af4": CoverageInfo(
                    args_before=[
                        '"fizzbuzz"',
                        '"mode"',
                        '"Before"',
                        "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
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
                "src.unit_test_generator.CoverageInfo",
                "logging.Manager",
                "logging.PlaceHolder",
                "logging.RootLogger",
                "logging.Logger",
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
                "81b0b79f99c4c6c8da805d371d799d98bbf771459f131f638d16e385ed46b84e": CoverageInfo(
                    args_before=[
                        "<function fizzbuzz at 0x0000020D1CBE3D80>",
                        "FunctionMetaData(name='fizzbuzz', parameter_names=['number'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/fizzbuzz/fizzbuzz.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_metadata",
                                "FunctionMetaData(name='fizzbuzz', parameter_names=['number'], is_method=False, lines=[40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57], non_code_lines={55}, global_vars_read_from={'mode'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/fizzbuzz/fizzbuzz.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'fizzbuzz': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\fizzbuzz\\\\fizzbuzz.py'})",
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
                "logging.StreamHandler",
                "src.unit_test_generator.FunctionMetaData",
                "logging.Manager",
                "pathlib.WindowsPath",
                "logging.RootLogger",
                "fizzbuzz.fizzbuzz",
                "logging.PlaceHolder",
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
        "fizzbuzz": FunctionMetaData(
            name="fizzbuzz",
            parameter_names=["number"],
            is_method=False,
            lines=[40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57],
            non_code_lines={55},
            global_vars_read_from={"mode"},
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/fizzbuzz/fizzbuzz.py"
            ),
            coverage_io={
                "2fcde918ffacbbb30ae860654c530d7850072b9a41fc16835cdc5bf0fdc3020d": CoverageInfo(
                    args_before=["30"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"mode": "fizzbuzz"},
                    globals_after={},
                    expected_result="30 with mode='fizzbuzz' yields 'fizzbuzz'",
                    expected_type="str",
                    coverage=[40, 41, 42, 43, 44, 45, 46, 47, 57],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                ),
                "332f74facbdc5888beeee5ca119926b4501c2dc9dd3ab99e811d6866bdd02840": CoverageInfo(
                    args_before=["30"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"mode": "buzzfizz"},
                    globals_after={},
                    expected_result="30 with mode='buzzfizz' yields 'buzzfizz'",
                    expected_type="str",
                    coverage=[40, 41, 48, 49, 50, 51, 52, 53, 54, 57],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                ),
                "458ae2906b3b144383bfba0618ff5c3ea1d2e981782eae30455d98eb608b4488": CoverageInfo(
                    args_before=["6"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"mode": "a_test"},
                    globals_after={},
                    expected_result="Mode 'a_test' invalid for fizzbuzz()",
                    expected_type="str",
                    coverage=[40, 41, 48, 56, 57],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                ),
            },
            coverage_percentage=100.0,
            types_in_use=set(),
            unified_test_coverage={
                40,
                41,
                42,
                43,
                44,
                45,
                46,
                47,
                48,
                49,
                50,
                51,
                52,
                53,
                54,
                56,
                57,
            },
            needs_pytest=False,
            callable_files={
                "fizzbuzz": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\fizzbuzz\\fizzbuzz.py"
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
                    "364dbab6e996d2b07a239c6ce2e2df688159375398cc8e1cb47de9677b4e0af4": CoverageInfo(
                        args_before=[
                            '"fizzbuzz"',
                            '"mode"',
                            '"Before"',
                            "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_coverage_info",
                                    "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                                )
                            ]
                        ),
                        kwargs={},
                        kwargs_after=OrderedDict(),
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
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
                    "logging.Logger",
                    "src.unit_test_generator.CoverageInfo",
                    "logging.Manager",
                    "logging.PlaceHolder",
                },
                unified_test_coverage={1607, 1610, 1615, 1623, 1624, 1627},
                needs_pytest=False,
                callable_files={
                    "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            {
                "364dbab6e996d2b07a239c6ce2e2df688159375398cc8e1cb47de9677b4e0af4": CoverageInfo(
                    args_before=[
                        '"fizzbuzz"',
                        '"mode"',
                        '"Before"',
                        "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
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
                "function_metadata": "FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1607, 1608, 1609, 1610, 1611, 1612, 1613, 1615, 1623, 1624, 1625, 1626, 1627], non_code_lines={1614, 1616, 1617, 1618, 1619, 1620, 1621, 1622}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'364dbab6e996d2b07a239c6ce2e2df688159375398cc8e1cb47de9677b4e0af4': CoverageInfo(args_before=['\"fizzbuzz\"','\"mode\"','\"Before\"',\"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after=OrderedDict([('this_coverage_info', \"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1607, 1610, 1615, 1623, 1624, 1627], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=46.15, types_in_use={'logging.StreamHandler', 'logging.RootLogger', 'logging.Logger', 'src.unit_test_generator.CoverageInfo', 'logging.Manager', 'logging.PlaceHolder'}, unified_test_coverage={1607, 1610, 1615, 1623, 1624, 1627}, needs_pytest=False, callable_files={'update_global': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
                "state": "{'364dbab6e996d2b07a239c6ce2e2df688159375398cc8e1cb47de9677b4e0af4': CoverageInfo(args_before=['\"fizzbuzz\"','\"mode\"','\"Before\"',\"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after={'this_coverage_info': \"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1607, 1610, 1615, 1623, 1624, 1627], exception_type='', exception_message='', constructor='', cost=0.0)}",
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
