"""
Programmatically generated test function for update_metadata()
"""

import re
import pytest
from divide_ints import divide_ints
from src import unit_test_generator

# Now import modules specific to update_metadata:
from logging import Logger
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath


# In sum, these tests covered 74.36% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1412', '1424', '1440-1442', '1449-1450']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, args_after",
    [
        (
            divide_ints,
            FunctionMetaData(
                name="divide_ints",
                parameter_names=["a", "b"],
                is_method=False,
                lines=[],
                non_code_lines=set(),
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/procedural_division/divide_ints.py"
                ),
                coverage_io={},
                coverage_percentage=0.0,
                types_in_use=set(),
                unified_test_coverage=set(),
                needs_pytest=False,
                callable_files={},
            ),
            "None",
            {
                "this_metadata": "FunctionMetaData(name='divide_ints', parameter_names=['a', 'b'], is_method=False, lines=[32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42], non_code_lines=set(), global_vars_read_from={'logger', 'error_code'}, global_vars_written_to={'error_code'}, source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/procedural_division/divide_ints.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'divide_ints': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\procedural_division\\\\divide_ints.py'})"
            },
        ),
    ],
)
def test_update_metadata(f, this_metadata, expected_result, args_after):
    """
    Programmatically generated test function for update_metadata()
    """
    result = unit_test_generator.update_metadata(f, this_metadata)
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_metadata == eval(args_after["this_metadata"])
        or args_after["this_metadata"] == this_metadata
    )
