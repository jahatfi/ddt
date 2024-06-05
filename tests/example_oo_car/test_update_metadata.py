"""
Programmatically generated test function for update_metadata()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_metadata:
from src.unit_test_generator import FunctionMetaData
from car import Car
from pathlib import WindowsPath


# In sum, these tests covered 69.23% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1122', '1133', '1139-1141', '1143-1145']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, expected_type",
    [
        (
            Car.__init__,
            FunctionMetaData(
                name="Car.__init__",
                parameter_names=["self", "color", "speed", "steer_angle"],
                is_method=True,
                lines=[],
                non_code_lines=set(),
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/example_oo_car/car.py"
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
