"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import CoverageInfo
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath


# In sum, these tests covered 50.0% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1600-1601', '1608-1610', '1614-1617', '1620', '1626-1627', '1632-1640', '1642', '1649', '1652', '1657-1662', '1669-1671', '1675', '1686-1687']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type",
    [
        (
            CoverageInfo(
                args=[
                    "all_types.get_item_at_index",
                    "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False)",
                ],
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="None",
                expected_type="NoneType",
                coverage=[
                    277,
                    278,
                    316,
                    318,
                    319,
                    320,
                    323,
                    324,
                    1081,
                    1083,
                    1084,
                    1085,
                    1086,
                    1087,
                    1089,
                    1090,
                    1091,
                    1092,
                    1104,
                    1105,
                    1108,
                    1111,
                    1121,
                    1123,
                    1125,
                    1126,
                    1127,
                    1128,
                    1129,
                    1131,
                    1132,
                    1134,
                    1135,
                    1136,
                    1137,
                    1138,
                    1139,
                    1140,
                    1142,
                    1146,
                    1147,
                    1148,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.004,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_metadata",
                parameter_names=["f", "this_metadata"],
                is_method=False,
                lines=[
                    1121,
                    1122,
                    1123,
                    1125,
                    1126,
                    1127,
                    1128,
                    1129,
                    1131,
                    1132,
                    1133,
                    1134,
                    1135,
                    1136,
                    1137,
                    1138,
                    1139,
                    1140,
                    1141,
                    1142,
                    1143,
                    1144,
                    1145,
                    1146,
                    1147,
                    1148,
                ],
                non_code_lines={1130, 1124},
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "d0eb5422a7465a482ca7ab729bea8d09b281bd64d24199fd626c0116ec46adaf": CoverageInfo(
                        args=[
                            "all_types.get_item_at_index",
                            "FunctionMetaData(name='get_item_at_index', parameter_names=['iterable', 'index'], is_method=False, lines=[], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False)",
                        ],
                        kwargs={},
                        globals_before={},
                        globals_after={},
                        expected_result="None",
                        expected_type="NoneType",
                        coverage=[
                            277,
                            278,
                            316,
                            318,
                            319,
                            320,
                            323,
                            324,
                            1081,
                            1083,
                            1084,
                            1085,
                            1086,
                            1087,
                            1089,
                            1090,
                            1091,
                            1092,
                            1104,
                            1105,
                            1108,
                            1111,
                            1121,
                            1123,
                            1125,
                            1126,
                            1127,
                            1128,
                            1129,
                            1131,
                            1132,
                            1134,
                            1135,
                            1136,
                            1137,
                            1138,
                            1139,
                            1140,
                            1142,
                            1146,
                            1147,
                            1148,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.004,
                    )
                },
                coverage_percentage=76.92,
                types_in_use={
                    "src.unit_test_generator.FunctionMetaData",
                    "pathlib.WindowsPath",
                    "logging.Logger",
                    "all_types",
                },
                unified_test_coverage={
                    1121,
                    1123,
                    1125,
                    1126,
                    1127,
                    1128,
                    1129,
                    1131,
                    1132,
                    1134,
                    1135,
                    1136,
                    1137,
                    1138,
                    1139,
                    1140,
                    1142,
                    1146,
                    1147,
                    1148,
                },
                needs_pytest=False,
            ),
            "['    result = unit_test_generator.update_metadata(f,this_metadata)\\n', '    assert result == expected_result or result == eval(expected_result)\\n']",
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
