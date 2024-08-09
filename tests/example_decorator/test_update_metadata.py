"""
Programmatically generated test function for update_metadata()
"""

import pytest
from decorator import add_ints
from src import unit_test_generator

# Now import modules specific to update_metadata:
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData


# In sum, these tests covered 65.0% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1209', '1221', '1233-1239', '1246-1247']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, expected_type, args_after",
    [
        (
            add_ints,
            FunctionMetaData(
                name="add_ints",
                parameter_names=["a", "b"],
                is_method=False,
                lines=[],
                non_code_lines=set(),
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/example_decorator/decorator.py"
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
                "this_metadata": "FunctionMetaData(name='add_ints', parameter_names=['a', 'b'], is_method=False, lines=[31], non_code_lines=set(), global_vars_read_from={'c'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/example_decorator/decorator.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'add_ints': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\example_decorator\\\\decorator.py'})"
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
    assert args_after["this_metadata"] == this_metadata or this_metadata == eval(
        args_after["this_metadata"]
    )
