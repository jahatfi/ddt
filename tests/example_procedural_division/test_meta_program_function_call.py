"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from pathlib import WindowsPath
from src.unit_test_generator import CoverageInfo
from src.unit_test_generator import FunctionMetaData


# In sum, these tests covered 50.67% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1552', '1578-1579', '1586-1588', '1592-1595', '1598', '1604-1605', '1610-1618', '1620', '1627', '1630', '1635-1640', '1647-1649', '1664-1665']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type",
    [
        (
            CoverageInfo(
                args=[
                    "0",
                    '"error_code"',
                    '"Before"',
                    "CoverageInfo(args=['6', '2'], kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                ],
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="CoverageInfo(args=['6', '2'], kwargs={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                expected_type="src.unit_test_generator.CoverageInfo",
                coverage=[1399, 1402, 1406, 1415, 1416, 1419],
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
                    1391,
                    1399,
                    1400,
                    1401,
                    1402,
                    1403,
                    1404,
                    1406,
                    1415,
                    1416,
                    1417,
                    1418,
                    1419,
                ],
                parameter_names=["obj", "this_global", "phase", "this_coverage_info"],
                is_method=False,
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "da43029a53540481556f16ea2f885298e81b420042c8a12d0a8e42c45a1c1cc3": CoverageInfo(
                        args=[
                            "0",
                            '"error_code"',
                            '"Before"',
                            "CoverageInfo(args=['6', '2'], kwargs={}, globals_before={}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        ],
                        kwargs={},
                        globals_before={},
                        globals_after={},
                        expected_result="CoverageInfo(args=['6', '2'], kwargs={}, globals_before={'error_code': 0}, globals_after={}, expected_result='', expected_type='', coverage=[], exception_type='', exception_message='', constructor='', cost=0.0)",
                        expected_type="src.unit_test_generator.CoverageInfo",
                        coverage=[1399, 1402, 1406, 1415, 1416, 1419],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.001,
                    )
                },
                coverage_percentage=46.15,
                types_in_use={"src.unit_test_generator.CoverageInfo", "logging.Logger"},
                unified_test_coverage={1415, 1416, 1419, 1399, 1402, 1406},
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
