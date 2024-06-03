"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import FunctionMetaData
from src.unit_test_generator import CoverageInfo
from pathlib import WindowsPath


# In sum, these tests covered 50.67% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1547', '1573-1574', '1581-1583', '1587-1590', '1593', '1599-1600', '1605-1613', '1615', '1622', '1625', '1630-1635', '1642-1644', '1659-1660']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type",
    [
        (
            CoverageInfo(
                args=[
                    "0",
                    '"method_call_counter"',
                    '"Before"',
                    "CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                ],
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                expected_type="src.unit_test_generator.CoverageInfo",
                coverage=[1394, 1397, 1401, 1410, 1411, 1414],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.001,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_global",
                lines=[
                    1386,
                    1394,
                    1395,
                    1396,
                    1397,
                    1398,
                    1399,
                    1401,
                    1410,
                    1411,
                    1412,
                    1413,
                    1414,
                ],
                parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
                is_method=False,
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "827ce9f30381c4cf8356fd85510849bde9e1eb403ab9893a609b1ffccaaf39eb": CoverageInfo(
                        args=[
                            "0",
                            '"method_call_counter"',
                            '"Before"',
                            "CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                        ],
                        kwargs={},
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args=['-1', '1'], kwargs={}, globals_before={'method_call_counter': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='Car(\"Red\", 10, 0)', cost=0.0)",
                        expected_type="src.unit_test_generator.CoverageInfo",
                        coverage=[1394, 1397, 1401, 1410, 1411, 1414],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.001,
                    )
                },
                coverage_percentage=46.15,
                types_in_use={"src.unit_test_generator.CoverageInfo", "logging.Logger"},
                unified_test_coverage={1410, 1411, 1414, 1394, 1397, 1401},
                needs_pytest=False,
            ),
            "['    result = unit_test_generator.update_global(obj,this_global,phase,this_coverage_info)\\n', '    assert isinstance(result, expected_type)\\n', '    assert result == expected_result or result == eval(expected_result)\\n']",
            list,
        ),
    ],
)
def test_meta_program_function_call(
    this_state, tab, package, function_metadata, expected_result, expected_type
):
    """
    Programmatically generated test function for meta_program_function_call()
    """
    result = unit_test_generator.meta_program_function_call(
        this_state, tab, package, function_metadata
    )
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
