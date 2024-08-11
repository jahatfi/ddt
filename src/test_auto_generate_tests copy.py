"""
Programmatically generated test function for auto_generate_tests()
"""

import re
import pytest
from src import unit_test_generator
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to auto_generate_tests:
from _io import TextIOWrapper
from logging import PlaceHolder
from logging import StreamHandler
from src.unit_test_generator import FunctionMetaData
from logging import Manager
from src.unit_test_generator import CoverageInfo
from pprint import PrettyPrinter
from collections import OrderedDict
from collections import defaultdict
from logging import RootLogger
from logging import Logger
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
            coverage_io={
                "bc219f43158bcf9bd56390fd2488dcf6143970ff6002221e94e29f0d72d381d9": CoverageInfo(
                    args_before=[
                        "0",
                        '"method_call_counter"',
                        '"Before"',
                        "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
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
                "logging.Manager",
                "logging.StreamHandler",
                "logging.Logger",
                "logging.RootLogger",
                "src.unit_test_generator.CoverageInfo",
                "logging.PlaceHolder",
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
                "a957a0aed8423c01c38d1111e384806112a73d4876a082ea2ca1421a6a95602a": CoverageInfo(
                    args_before=[
                        'Car("Red", 10, 0)',
                        "FunctionMetaData(name='Car.__init__', parameter_names=['self', 'color', 'speed', 'steer_angle'], is_method=True, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={})",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_metadata",
                                "FunctionMetaData(name='Car.__init__', parameter_names=['self', 'color', 'speed', 'steer_angle'], is_method=True, lines=[41, 42, 43], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'__init__': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\oo_car\\\\car.py'})",
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
                    cost=0.0,
                )
            },
            coverage_percentage=56.41,
            types_in_use={
                "logging.Manager",
                "pathlib.WindowsPath",
                "logging.Logger",
                "logging.StreamHandler",
                "src.unit_test_generator.FunctionMetaData",
                "logging.RootLogger",
                "car.Car",
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
        "Car.__init__": FunctionMetaData(
            name="Car.__init__",
            parameter_names=["self", "color", "speed", "steer_angle"],
            is_method=True,
            lines=[41, 42, 43],
            non_code_lines=set(),
            global_vars_read_from=set(),
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py"
            ),
            coverage_io={
                "c878113de933bc35ec08d5024d0aae800d76ba42b32be7f1075b8a7586805a2c": CoverageInfo(
                    args_before=['"Red"', "10", "0"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[41, 42, 43],
                    exception_type="",
                    exception_message="",
                    constructor="",
                    cost=0.0,
                )
            },
            coverage_percentage=100.0,
            types_in_use=set(),
            unified_test_coverage={41, 42, 43},
            needs_pytest=False,
            callable_files={
                "__init__": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\oo_car\\car.py"
            },
        ),
        "Car.gas": FunctionMetaData(
            name="Car.gas",
            parameter_names=["self", "rate", "duration"],
            is_method=True,
            lines=[66, 67, 68, 69, 70, 71],
            non_code_lines=set(),
            global_vars_read_from={"method_call_counter", "logger"},
            global_vars_written_to={"method_call_counter"},
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py"
            ),
            coverage_io={
                "78e4f6e57c2f532c43747e020340acf548111ebba3a4dfbb9b7a12af2d0fa659": CoverageInfo(
                    args_before=["-1", "1"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"method_call_counter": 0},
                    globals_after={"method_call_counter": 1},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[66, 67, 68, 69],
                    exception_type="<class 'ValueError'>",
                    exception_message="Gas rate (m/s) must be positive.",
                    constructor='Car("Red", 10, 0)',
                    cost=0.0,
                ),
                "6489cc7d9835b1fc422a9e25a2d99a7374cf0a90d0450a9435df3167635e432a": CoverageInfo(
                    args_before=["2", "2"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={"method_call_counter": 1},
                    globals_after={"method_call_counter": 2},
                    expected_result="16",
                    expected_type="int",
                    coverage=[66, 67, 68, 70, 71],
                    exception_type="",
                    exception_message="",
                    constructor='Car("White", 12, -30)',
                    cost=0.0,
                ),
            },
            coverage_percentage=100.0,
            types_in_use={
                "tests.oo_car.car.Car",
                "logging.Manager",
                "logging.StreamHandler",
                "logging.Logger",
                "logging.RootLogger",
                "logging.PlaceHolder",
            },
            unified_test_coverage={66, 67, 68, 69, 70, 71},
            needs_pytest=True,
            callable_files={
                "gas": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\oo_car\\car.py"
            },
        ),
        "Car.brake": FunctionMetaData(
            name="Car.brake",
            parameter_names=["self", "rate", "duration"],
            is_method=True,
            lines=[50, 51, 52, 53, 54, 55, 56],
            non_code_lines=set(),
            global_vars_read_from={"logger"},
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py"
            ),
            coverage_io={
                "79d14ba2847338fe6989a7d3640887679f88b2cfadee250647df044fe4abc0b9": CoverageInfo(
                    args_before=["-1", "1"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="9",
                    expected_type="int",
                    coverage=[50, 51, 53, 55, 56],
                    exception_type="",
                    exception_message="",
                    constructor='Car("Red", 10, 0)',
                    cost=0.0,
                )
            },
            coverage_percentage=71.43,
            types_in_use={
                "tests.oo_car.car.Car",
                "logging.Manager",
                "logging.StreamHandler",
                "logging.Logger",
                "logging.RootLogger",
                "logging.PlaceHolder",
            },
            unified_test_coverage={50, 51, 53, 55, 56},
            needs_pytest=False,
            callable_files={
                "brake": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\oo_car\\car.py"
            },
        ),
        "Car.change_steer_angle": FunctionMetaData(
            name="Car.change_steer_angle",
            parameter_names=["self", "angle"],
            is_method=True,
            lines=[79, 80, 81, 83, 86, 87, 86, 88, 86, 90],
            non_code_lines={89, 82, 84, 85},
            global_vars_read_from={"logger"},
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py"
            ),
            coverage_io={
                "9e5729283fb4205cc004e81e18786a627d2eb0f21140111b0a77b56ac7ded037": CoverageInfo(
                    args_before=["30"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="30",
                    expected_type="int",
                    coverage=[79, 80, 83, 86, 90],
                    exception_type="",
                    exception_message="",
                    constructor='Car("Red", 9, 0)',
                    cost=0.0,
                ),
                "78fd5f6e8e8bd7118d1ec9602907dd07a7495e42f6814cd047a8057a96388cd7": CoverageInfo(
                    args_before=["90"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="60",
                    expected_type="int",
                    coverage=[79, 80, 83, 86, 90],
                    exception_type="",
                    exception_message="",
                    constructor='Car("White", 20, -30)',
                    cost=0.0,
                ),
                "4e6967deeb4e51bab447208d79037a8bca61cdf648fb62d21885290b177313f6": CoverageInfo(
                    args_before=["180"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="210",
                    expected_type="int",
                    coverage=[79, 80, 83, 86, 90],
                    exception_type="",
                    exception_message="",
                    constructor='Car("Blue", 0.0, 30)',
                    cost=0.0,
                ),
                "9da25bda4c0856a5b359c8df1d926a3ed762a3d8f6f58108d234a201cb75d875": CoverageInfo(
                    args_before=["-1080"],
                    args_after=OrderedDict(),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="None",
                    expected_type="NoneType",
                    coverage=[79, 80, 81],
                    exception_type="<class 'AssertionError'>",
                    exception_message="angle=-1080    out of bounds!",
                    constructor='Car("Green", 48, 90)',
                    cost=0.0,
                ),
            },
            coverage_percentage=60.0,
            types_in_use={
                "tests.oo_car.car.Car",
                "logging.Manager",
                "logging.StreamHandler",
                "logging.Logger",
                "logging.RootLogger",
                "logging.PlaceHolder",
            },
            unified_test_coverage={79, 80, 81, 83, 86, 90},
            needs_pytest=True,
            callable_files={
                "change_steer_angle": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\oo_car\\car.py"
            },
        ),
        "Car.is_going_faster_than": FunctionMetaData(
            name="Car.is_going_faster_than",
            parameter_names=["self", "other_car"],
            is_method=True,
            lines=[126],
            non_code_lines=set(),
            global_vars_read_from=set(),
            global_vars_written_to=set(),
            source_file=WindowsPath(
                "C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py"
            ),
            coverage_io={
                "797ee52405b6b24f04cee9d62d992fd2a5592ed30653401b854ee509666247fc": CoverageInfo(
                    args_before=['Car("White", 19, 0)'],
                    args_after=OrderedDict([("other_car", 'Car("White", 19, 0)')]),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="True",
                    expected_type="bool",
                    coverage=[126],
                    exception_type="",
                    exception_message="",
                    constructor='Car("Red", 20, 0)',
                    cost=0.0,
                )
            },
            coverage_percentage=100.0,
            types_in_use={"__main__.Car", "tests.oo_car.car.Car"},
            unified_test_coverage={126},
            needs_pytest=False,
            callable_files={
                "is_going_faster_than": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\tests\\oo_car\\car.py"
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
                    "bc219f43158bcf9bd56390fd2488dcf6143970ff6002221e94e29f0d72d381d9": CoverageInfo(
                        args_before=[
                            "0",
                            '"method_call_counter"',
                            '"Before"',
                            "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                        ],
                        args_after=OrderedDict(
                            [
                                (
                                    "this_coverage_info",
                                    "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                                )
                            ]
                        ),
                        kwargs={},
                        kwargs_after=OrderedDict(),
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
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
                    "logging.Manager",
                    "logging.RootLogger",
                    "logging.StreamHandler",
                    "logging.Logger",
                    "src.unit_test_generator.CoverageInfo",
                    "logging.PlaceHolder",
                },
                unified_test_coverage={1602, 1607, 1615, 1616, 1619, 1599},
                needs_pytest=False,
                callable_files={
                    "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            {
                "bc219f43158bcf9bd56390fd2488dcf6143970ff6002221e94e29f0d72d381d9": CoverageInfo(
                    args_before=[
                        "0",
                        '"method_call_counter"',
                        '"Before"',
                        "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                    ],
                    args_after=OrderedDict(
                        [
                            (
                                "this_coverage_info",
                                "CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                            )
                        ]
                    ),
                    kwargs={},
                    kwargs_after=OrderedDict(),
                    globals_before={},
                    globals_after={},
                    expected_result="CoverageInfo(args_before=['-1', '1'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
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
                "function_metadata": "FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1599, 1600, 1601, 1602, 1603, 1604, 1605, 1607, 1615, 1616, 1617, 1618, 1619], non_code_lines={1606, 1608, 1609, 1610, 1611, 1612, 1613, 1614}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'bc219f43158bcf9bd56390fd2488dcf6143970ff6002221e94e29f0d72d381d9': CoverageInfo(args_before=['0', '\"method_call_counter\"', '\"Before\"', 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)'], args_after=OrderedDict([('this_coverage_info', 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, kwargs_after={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)')]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, kwargs_after={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)', expected_type='src.unit_test_generator.CoverageInfo', coverage=[1599, 1602, 1607, 1615, 1616, 1619], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=46.15, types_in_use={'logging.Manager', 'logging.RootLogger', 'logging.StreamHandler', 'logging.Logger', 'src.unit_test_generator.CoverageInfo', 'logging.PlaceHolder'}, unified_test_coverage={1602, 1607, 1615, 1616, 1619, 1599}, needs_pytest=False, callable_files={'update_global': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
                "state": "{'bc219f43158bcf9bd56390fd2488dcf6143970ff6002221e94e29f0d72d381d9': CoverageInfo(args_before=['0', '\"method_call_counter\"', '\"Before\"', 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)'], args_after={'this_coverage_info': 'CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, kwargs_after={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)'}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result='CoverageInfo(args_before=[\\'-1\\', \\'1\\'], args_after={}, kwargs={}, kwargs_after={}, globals_before={\\'method_call_counter\\': 0}, globals_after={}, expected_result=\\'\\', expected_type=\\'\\', coverage=[], exception_type=\\'\\', exception_message=\\'\\', constructor=\\'Car(\"Red\", 10, 0)\\', cost=0.0)', expected_type='src.unit_test_generator.CoverageInfo', coverage=[1599, 1602, 1607, 1615, 1616, 1619], exception_type='', exception_message='', constructor='', cost=0.0)}",
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
