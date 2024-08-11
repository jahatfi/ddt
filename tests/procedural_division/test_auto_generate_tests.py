"""
Programmatically generated test function for auto_generate_tests()
"""

import pytest
from src import unit_test_generator
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to auto_generate_tests:
from pathlib import WindowsPath
from collections import OrderedDict
from src.unit_test_generator import CoverageInfo
from collections import defaultdict
from src.unit_test_generator import FunctionMetaData

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
            coverage_io={
                "03a61bab75c52bb0770f60d8549ba350d2b9a21795735ab9fbb017959c6e9eed": CoverageInfo(
                    args_before=[
                        "0",
                        '"error_code"',
                        '"Before"',
                        "CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    expected_type="src.unit_test_generator.CoverageInfo",
                    coverage=[1599, 1602, 1607, 1615, 1616, 1619],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            coverage_percentage=46.15,
            types_in_use={
                "src.unit_test_generator.CoverageInfo",
                "logging.StreamHandler",
                "logging.RootLogger",
                "logging.Logger",
                "logging.PlaceHolder",
                "logging.Manager",
            },
            unified_test_coverage={1602, 1607, 1615, 1616, 1619, 1599},
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
                "3325a35f1269947fdeeb998ef8b30878c618a9e36cf484df23ef1532c72dffc2": CoverageInfo(
                    args_before=[
                        "<function divide_ints at 0x000002C74E0904A0>",
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
                        1445,
                        1447,
                        1448,
                        1449,
                        1450,
                        1451,
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
                    cost=0.0,
                )
            },
            coverage_percentage=74.36,
            types_in_use={
                "logging.Manager",
                "pathlib.WindowsPath",
                "logging.StreamHandler",
                "logging.RootLogger",
                "logging.Logger",
                "logging.PlaceHolder",
                "divide_ints.divide_ints",
                "src.unit_test_generator.FunctionMetaData",
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
                1445,
                1447,
                1448,
                1449,
                1450,
                1451,
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
                "logging.RootLogger",
                "logging.StreamHandler",
                "logging.Logger",
                "logging.PlaceHolder",
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


# In sum, these tests covered 49.4% of auto_generate_tests's lines
# Line(s) not covered by ANY of the tests below:
# ['2048-2049', '2051-2052', '2054', '2056-2057', '2059-2061', '2063', '2068', '2070', '2074', '2086-2087', '2091-2094', '2096', '2098', '2104-2110', '2121', '2125', '2127-2128', '2130-2135', '2137', '2139-2140', '2142-2144', '2147', '2149', '2154', '2156', '2158-2159', '2163-2165', '2169-2180', '2190', '2194', '2209', '2219-2220', '2222', '2227-2228', '2230-2231', '2251-2253', '2271-2272', '2274-2279', '2285-2286', '2288-2293', '1899', '1918-1923', '1925-1926', '1928-1929', '1939-1942', '1944-1949', '1951-1953', '1963-1964', '1977-1978', '1980', '1998', '2002-2003', '2005-2006', '2012-2013', '2015-2016', '2018-2019', '2026', '2029-2030', '2037', '2041-2047']
@pytest.mark.parametrize(
    "function_metadata, state, function_name, source_file, tests_dir, outdir, indent_size, expected_result, args_after, globals_before",
    [
        (
            FunctionMetaData(
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
                coverage_io={
                    "03a61bab75c52bb0770f60d8549ba350d2b9a21795735ab9fbb017959c6e9eed": CoverageInfo(
                        args_before=[
                            "0",
                            '"error_code"',
                            '"Before"',
                            "CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_coverage_info",
                                    "CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                                )
                            ]
                        ),
                        kwargs={},
                        kwargs_after=OrderedDict(),
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        expected_type="src.unit_test_generator.CoverageInfo",
                        coverage=[1599, 1602, 1607, 1615, 1616, 1619],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.0,
                    )
                },
                coverage_percentage=46.15,
                types_in_use={
                    "logging.Logger",
                    "logging.RootLogger",
                    "src.unit_test_generator.CoverageInfo",
                    "logging.PlaceHolder",
                    "logging.Manager",
                    "logging.StreamHandler",
                },
                unified_test_coverage={1602, 1607, 1615, 1616, 1619, 1599},
                needs_pytest=False,
                callable_files={
                    "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            {
                "03a61bab75c52bb0770f60d8549ba350d2b9a21795735ab9fbb017959c6e9eed": CoverageInfo(
                    args_before=[
                        "0",
                        '"error_code"',
                        '"Before"',
                        "CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                    expected_type="src.unit_test_generator.CoverageInfo",
                    coverage=[1599, 1602, 1607, 1615, 1616, 1619],
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
                "function_metadata": "FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1599, 1600, 1601, 1602, 1603, 1604, 1605, 1607, 1615, 1616, 1617, 1618, 1619], non_code_lines={1606, 1608, 1609, 1610, 1611, 1612, 1613, 1614}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'03a61bab75c52bb0770f60d8549ba350d2b9a21795735ab9fbb017959c6e9eed': CoverageInfo(args_before=['0', '\"error_code\"', '\"Before\"', \"CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after=OrderedDict([('this_coverage_info', \"CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1599, 1602, 1607, 1615, 1616, 1619], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=46.15, types_in_use={'logging.Logger', 'logging.RootLogger', 'src.unit_test_generator.CoverageInfo', 'logging.PlaceHolder', 'logging.Manager', 'logging.StreamHandler'}, unified_test_coverage={1602, 1607, 1615, 1616, 1619, 1599}, needs_pytest=False, callable_files={'update_global': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
                "state": "{'03a61bab75c52bb0770f60d8549ba350d2b9a21795735ab9fbb017959c6e9eed': CoverageInfo(args_before=['0', '\"error_code\"', '\"Before\"', \"CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after={'this_coverage_info': \"CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6', '2'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1599, 1602, 1607, 1615, 1616, 1619], exception_type='', exception_message='', constructor='', cost=0.0)}",
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
