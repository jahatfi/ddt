"""
Programmatically generated test function for meta_program_function_call()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to meta_program_function_call:
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath
from src.unit_test_generator import CoverageInfo


# In sum, these tests covered 50.0% of meta_program_function_call's lines
# Line(s) not covered by ANY of the tests below:
# ['1599-1600', '1607-1609', '1613-1616', '1619', '1625-1626', '1631-1639', '1641', '1648', '1651', '1656-1661', '1668-1670', '1674', '1685-1686']
@pytest.mark.parametrize(
    "this_state, tab, package, function_metadata, expected_result, expected_type",
    [
        (
            CoverageInfo(
                args=[
                    "all_types.get_item_at_index",
                    "FunctionMetaData(name='get_item_at_index', lines=[], parameter_names=['iterable', 'index'], is_method=False, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False)",
                ],
                kwargs={},
                globals_before={},
                globals_after={},
                expected_result="None",
                expected_type="NoneType",
                coverage=[
                    276,
                    277,
                    315,
                    317,
                    318,
                    319,
                    322,
                    323,
                    1080,
                    1082,
                    1083,
                    1084,
                    1085,
                    1086,
                    1088,
                    1089,
                    1090,
                    1091,
                    1103,
                    1104,
                    1107,
                    1110,
                    1120,
                    1122,
                    1124,
                    1125,
                    1126,
                    1127,
                    1128,
                    1130,
                    1131,
                    1133,
                    1134,
                    1135,
                    1136,
                    1137,
                    1138,
                    1139,
                    1141,
                    1145,
                    1146,
                    1147,
                ],
                exception_type="",
                exception_message="",
                constructor="",
                cost=0.005,
            ),
            "  ",
            "unit_test_generator",
            FunctionMetaData(
                name="update_metadata",
                lines=[
                    1120,
                    1121,
                    1122,
                    1124,
                    1125,
                    1126,
                    1127,
                    1128,
                    1130,
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
                ],
                parameter_names=["f", "this_metadata"],
                is_method=False,
                global_vars_read_from={"logger"},
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/src/unit_test_generator.py"
                ),
                coverage_io={
                    "975a2a3a4a98049f16a0603581ef567c032bad79d9e8a3065948172922a55521": CoverageInfo(
                        args=[
                            "all_types.get_item_at_index",
                            "FunctionMetaData(name='get_item_at_index', lines=[], parameter_names=['iterable', 'index'], is_method=False, global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False)",
                        ],
                        kwargs={},
                        globals_before={},
                        globals_after={},
                        expected_result="None",
                        expected_type="NoneType",
                        coverage=[
                            276,
                            277,
                            315,
                            317,
                            318,
                            319,
                            322,
                            323,
                            1080,
                            1082,
                            1083,
                            1084,
                            1085,
                            1086,
                            1088,
                            1089,
                            1090,
                            1091,
                            1103,
                            1104,
                            1107,
                            1110,
                            1120,
                            1122,
                            1124,
                            1125,
                            1126,
                            1127,
                            1128,
                            1130,
                            1131,
                            1133,
                            1134,
                            1135,
                            1136,
                            1137,
                            1138,
                            1139,
                            1141,
                            1145,
                            1146,
                            1147,
                        ],
                        exception_type="",
                        exception_message="",
                        constructor="",
                        cost=0.005,
                    )
                },
                coverage_percentage=76.92,
                types_in_use={
                    "logging.Logger",
                    "src.unit_test_generator.FunctionMetaData",
                    "pathlib.WindowsPath",
                    "all_types",
                },
                unified_test_coverage={
                    1120,
                    1122,
                    1124,
                    1125,
                    1126,
                    1127,
                    1128,
                    1130,
                    1131,
                    1133,
                    1134,
                    1135,
                    1136,
                    1137,
                    1138,
                    1139,
                    1141,
                    1145,
                    1146,
                    1147,
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
