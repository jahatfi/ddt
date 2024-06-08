"""
Programmatically generated test function for update_metadata()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_metadata:
import divide_ints
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData


# In sum, these tests covered 92.31% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1123']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, expected_type",
    [
        (
            divide_ints.divide_ints,
            FunctionMetaData(
                name="divide_ints",
                parameter_names=["a", "b"],
                is_method=False,
                lines=[],
                non_code_lines=set(),
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/example_procedural_division/divide_ints.py"
                ),
                coverage_io={},
                coverage_percentage=0.0,
                types_in_use=set(),
                unified_test_coverage=set(),
                needs_pytest=False,
            ),
            "None",
            "N/A",
        ),
    ],
)
def test_update_metadata(f, this_metadata, expected_result, expected_type):
    """
    Programmatically generated test function for update_metadata()
    """
    result = unit_test_generator.update_metadata(f, this_metadata)
    assert result == expected_result or result == eval(expected_result)
