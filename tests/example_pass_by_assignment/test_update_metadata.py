"""
Programmatically generated test function for update_metadata()
"""

import pytest
from pass_by_assignment import append_list
from src import unit_test_generator

# Now import modules specific to update_metadata:
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData


# In sum, these tests covered 64.1% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1214', '1226', '1238-1244', '1251-1252']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, expected_type, args_after",
    [
        (
            append_list,
            FunctionMetaData(
                name="append_list",
                parameter_names=["this_list", "item"],
                is_method=False,
                lines=[],
                non_code_lines=set(),
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/example_pass_by_assignment/pass_by_assignment.py"
                ),
                coverage_io={},
                coverage_percentage=0.0,
                types_in_use=set(),
                unified_test_coverage=set(),
                needs_pytest=False,
                callable_files={},
            ),
            "None",
            "N/A",
            {
                "this_metadata": "FunctionMetaData(name='append_list', parameter_names=['this_list', 'item'], is_method=False, lines=[31, 32], non_code_lines=set(), global_vars_read_from={'logger'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_pass_by_assignment/pass_by_assignment.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'append_list': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\example_pass_by_assignment\\\\pass_by_assignment.py'})"
            },
        ),
    ],
)
def test_update_metadata(f, this_metadata, expected_result, expected_type, args_after):
    """
    Programmatically generated test function for update_metadata()
    """
    result = unit_test_generator.update_metadata(f, this_metadata)
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_metadata == eval(args_after["this_metadata"])
        or args_after["this_metadata"] == this_metadata
    )
