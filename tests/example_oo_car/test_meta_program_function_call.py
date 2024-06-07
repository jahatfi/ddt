"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 51.35% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1601-1602', '1609-1611', '1615-1618', '1621', '1627-1628', '1633-1641', '1643', '1650', '1653', '1658-1663', '1670-1672', '1687-1688']
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
                coverage=[1421, 1424, 1428, 1437, 1438, 1441],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.001,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_global",
                parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
                is_method=False,
                lines=[
                    1421,
                    1422,
                    1423,
                    1424,
                    1425,
                    1426,
                    1428,
                    1437,
                    1438,
                    1439,
                    1440,
                    1441,
                ],
                non_code_lines={1427, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436},
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
                        coverage=[1421, 1424, 1428, 1437, 1438, 1441],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.001,
                    )
                },
                coverage_percentage=50.0,
                types_in_use={"logging.Logger", "src.unit_test_generator.CoverageInfo"},
                unified_test_coverage={1441, 1421, 1424, 1428, 1437, 1438},
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
