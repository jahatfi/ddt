"""
Programmatically generated test function for update_metadata()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_metadata:
from pathlib import WindowsPath
import fizzbuzz
from src.unit_test_generator import FunctionMetaData


# In sum, these tests covered 84.85% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1152', '1121', '1140', '1150-1151']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, expected_type",
    [
        (
            fizzbuzz.fizzbuzz,
            FunctionMetaData(
                name="fizzbuzz",
                lines=[],
                parameter_names=["number"],
                is_method=False,
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/example_fizzbuzz/fizzbuzz.py"
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
