"""
Programmatically generated test function for update_metadata()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_metadata:
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData
import all_types


# In sum, these tests covered 81.82% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1152', '1121', '1140', '1148', '1150-1151']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, expected_type",
    [
        (
            all_types.get_item_at_index,
            FunctionMetaData(
                name="get_item_at_index",
                lines=[],
                parameter_names=["iterable", "index"],
                is_method=False,
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/example_all_types/all_types.py"
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
