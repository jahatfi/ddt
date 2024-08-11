"""
Programmatically generated test function for update_metadata()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to update_metadata:
from car import Car
from src.unit_test_generator import FunctionMetaData
from pathlib import WindowsPath


# In sum, these tests covered 56.41% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1424', '1436', '1442-1443', '1445', '1448-1454', '1461-1462']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, args_after",
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
                    "C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py"
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
                "this_metadata": "FunctionMetaData(name='Car.__init__', parameter_names=['self', 'color', 'speed', 'steer_angle'], is_method=True, lines=[41, 42, 43], non_code_lines=set(), global_vars_read_from=set(), global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/oo_car/car.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'__init__': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\oo_car\\\\car.py'})"
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
