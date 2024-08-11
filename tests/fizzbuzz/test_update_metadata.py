"""
Programmatically generated test function for update_metadata()
"""

import re
import pytest
from fizzbuzz import fizzbuzz
from src import unit_test_generator

# Now import modules specific to update_metadata:
from logging import Logger
from pathlib import WindowsPath
from src.unit_test_generator import FunctionMetaData
from logging import Manager
from logging import PlaceHolder
from logging import StreamHandler
from logging import RootLogger
from fizzbuzz import fizzbuzz


# In sum, these tests covered 64.1% of update_metadata's lines
# Line(s) not covered by ANY of the tests below:
# ['1429', '1441', '1453-1459', '1466-1467']
@pytest.mark.parametrize(
    "f, this_metadata, expected_result, args_after",
    [
        (
            fizzbuzz,
            FunctionMetaData(
                name="fizzbuzz",
                parameter_names=["number"],
                is_method=False,
                lines=[],
                non_code_lines=set(),
                global_vars_read_from=set(),
                global_vars_written_to=set(),
                source_file=WindowsPath(
                    "C:/Users/James/Documents/CyberResources/ddt/tests/fizzbuzz/fizzbuzz.py"
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
                "this_metadata": "FunctionMetaData(name='fizzbuzz', parameter_names=['number'], is_method=False, lines=[40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57], non_code_lines={55}, global_vars_read_from={'mode'}, global_vars_written_to=set(), source_file=WindowsPath('C:/Users/James/Documents/CyberResources/ddt/tests/fizzbuzz/fizzbuzz.py'), coverage_io={}, coverage_percentage=0.0, types_in_use=set(), unified_test_coverage=set(), needs_pytest=False, callable_files={'fizzbuzz': 'C:\\\\Users\\\\James\\\\Documents\\\\CyberResources\\\\ddt\\\\tests\\\\fizzbuzz\\\\fizzbuzz.py'})"
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
