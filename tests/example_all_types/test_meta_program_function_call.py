"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath


# In sum, these tests covered 52.0% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1552', '1578-1579', '1586-1588', '1592-1595', '1598', '1603', '1610-1618', '1620', '1627', '1630', '1635-1640', '1647-1649', '1664-1665']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type",
    [
        (
            CoverageInfo(
                args=["all_types.get_item_at_index"],
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
                expected_type="list",
                coverage=[
                    1060,
                    1062,
                    1063,
                    1064,
                    1065,
                    1066,
                    1068,
                    1069,
                    1070,
                    1071,
                    1083,
                    1084,
                    1087,
                    1090,
                    1100,
                    1102,
                    1104,
                    1105,
                    1106,
                    1107,
                    1108,
                    1109,
                    1110,
                    1111,
                    1112,
                    1113,
                    1114,
                    1115,
                    1116,
                    1117,
                    1119,
                    1123,
                    1128,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.002,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="return_function_line_numbers_and_accessed_globals",
                lines=[
                    1092,
                    1100,
                    1101,
                    1102,
                    1104,
                    1105,
                    1106,
                    1107,
                    1108,
                    1109,
                    1110,
                    1111,
                    1112,
                    1113,
                    1114,
                    1115,
                    1116,
                    1117,
                    1118,
                    1119,
                    1120,
                    1121,
                    1122,
                    1124,
                    1125,
                    1126,
                    1123,
                    1128,
                ],
                parameter_names=["f"],
                is_method=False,
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "25a6147ef8a293e4fb92826c38d1e35595fa4ba1c383353b8444ce66c3f23e54": CoverageInfo(
                        args=["all_types.get_item_at_index"],
                        kwargs={},
                        globals_before={},
                        globals_after={},
                        expected_result="[[22, 29, 30, 31, 32, 33, 34, 36], set(), set()]",
                        expected_type="list",
                        coverage=[
                            1060,
                            1062,
                            1063,
                            1064,
                            1065,
                            1066,
                            1068,
                            1069,
                            1070,
                            1071,
                            1083,
                            1084,
                            1087,
                            1090,
                            1100,
                            1102,
                            1104,
                            1105,
                            1106,
                            1107,
                            1108,
                            1109,
                            1110,
                            1111,
                            1112,
                            1113,
                            1114,
                            1115,
                            1116,
                            1117,
                            1119,
                            1123,
                            1128,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.002,
                    )
                },
                coverage_percentage=67.86,
                types_in_use={"all_types", "logging.Logger"},
                unified_test_coverage={
                    1100,
                    1102,
                    1104,
                    1105,
                    1106,
                    1107,
                    1108,
                    1109,
                    1110,
                    1111,
                    1112,
                    1113,
                    1114,
                    1115,
                    1116,
                    1117,
                    1119,
                    1123,
                    1128,
                },
                needs_pytest=False,
            ),
            "['    result = unit_test_generator.return_function_line_numbers_and_accessed_globals(f)\\n', '    assert isinstance(result, expected_type)\\n', '    assert result == expected_result or result == eval(expected_result)\\n']",
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
