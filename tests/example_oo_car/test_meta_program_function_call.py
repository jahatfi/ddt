"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import FunctionMetaData
from src.unit_test_generator import CoverageInfo
from pathlib import WindowsPath


# In sum, these tests covered 51.35% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1599-1600', '1607-1609', '1613-1616', '1619', '1625-1626', '1631-1639', '1641', '1648', '1651', '1656-1661', '1668-1670', '1685-1686']
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
                coverage=[1419, 1422, 1426, 1435, 1436, 1439],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.002,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_global",
                lines=[
                    1419,
                    1420,
                    1421,
                    1422,
                    1423,
                    1424,
                    1426,
                    1435,
                    1436,
                    1437,
                    1438,
                    1439,
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
                        coverage=[1419, 1422, 1426, 1435, 1436, 1439],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.002,
                    )
                },
                coverage_percentage=50.0,
                types_in_use={"logging.Logger", "src.unit_test_generator.CoverageInfo"},
                unified_test_coverage={1419, 1422, 1426, 1435, 1436, 1439},
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
