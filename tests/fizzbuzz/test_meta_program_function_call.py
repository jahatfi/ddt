"""
Programmatically generated test function for meta_program_function_call()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from collections import OrderedDict
from logging import Logger
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData
from logging import Manager
from src.unit_test_generator import CoverageInfo
from logging import PlaceHolder
from logging import StreamHandler
from logging import RootLogger


# In sum, these tests covered 51.95% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1793-1794', '1798-1801', '1804', '1810-1811', '1816-1824', '1826', '1833', '1836', '1841-1846', '1853-1855', '1874-1875', '1878-1879', '1783-1784']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, args_after",
    [
        (
            CoverageInfo(
                args_before=[
                    '"fizzbuzz"',
                    '"mode"',
                    '"Before"',
                    "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                ],
                args_after={
                    "this_coverage_info": "CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)"
                },
                kwargs={},
                kwargs_after=OrderedDict(),
                globals_before={},
                globals_after={},
                expected_result="CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                expected_type="src.unit_test_generator.CoverageInfo",
                coverage=[1603, 1606, 1611, 1619, 1620, 1623],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.0,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_global",
                parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
                is_method=False,
                lines=[
                    1603,
                    1604,
                    1605,
                    1606,
                    1607,
                    1608,
                    1609,
                    1611,
                    1619,
                    1620,
                    1621,
                    1622,
                    1623,
                ],
                non_code_lines={1610, 1612, 1613, 1614, 1615, 1616, 1617, 1618},
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
                        coverage=[1603, 1606, 1611, 1619, 1620, 1623],
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
                unified_test_coverage={1603, 1606, 1611, 1619, 1620, 1623},
                needs_pytest=False,
                callable_files={
                    "update_global": "C:\\Users\\James\\Documents\\CyberResources\\ddt\\src\\unit_test_generator.py"
                },
            ),
            "['    result = unit_test_generator.update_global(obj,this_global,phase,this_coverage_info)\\n', '    assert result == expected_result or result == eval(expected_result)\\n', '    assert this_coverage_info == eval(args_after[\"this_coverage_info\"]) or args_after[\"this_coverage_info\"] == this_coverage_info\\n']",
            {
                "this_state": "CoverageInfo(args_before=['\"fizzbuzz\"', '\"mode\"', '\"Before\"', \"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after={'this_coverage_info': \"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"}, kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1603, 1606, 1611, 1619, 1620, 1623], exception_type='', exception_message='', constructor='', cost=0.0)",
                "function_metadata": "FunctionMetaData(name='update_global', parameter_names=['obj', 'this_global', 'phase', 'this_coverage_info'], is_method=False, lines=[1603, 1604, 1605, 1606, 1607, 1608, 1609, 1611, 1619, 1620, 1621, 1622, 1623], non_code_lines={1610, 1612, 1613, 1614, 1615, 1616, 1617, 1618}, global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py'), coverage_io={'364dbab6e996d2b07a239c6ce2e2df688159375398cc8e1cb47de9677b4e0af4': CoverageInfo(args_before=['\"fizzbuzz\"', '\"mode\"', '\"Before\"', \"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\"], args_after=OrderedDict([('this_coverage_info', \"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\")]), kwargs={}, kwargs_after=OrderedDict(), globals_before={}, globals_after={}, expected_result=\"CoverageInfo(args_before=['6'], args_after={}, kwargs={}, kwargs_after={}, globals_before={'mode': 'fizzbuzz'}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)\", expected_type='src.unit_test_generator.CoverageInfo', coverage=[1603, 1606, 1611, 1619, 1620, 1623], exception_type='', exception_message='', constructor='', cost=0.0)}, coverage_percentage=46.15, types_in_use={'logging.Logger', 'logging.StreamHandler', 'logging.RootLogger', 'logging.Manager', 'logging.PlaceHolder', 'src.unit_test_generator.CoverageInfo'}, unified_test_coverage={1603, 1606, 1611, 1619, 1620, 1623}, needs_pytest=False, callable_files={'update_global': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\src\\\\unit_test_generator.py'})",
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
