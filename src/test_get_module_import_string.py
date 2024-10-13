"""
Programmatically generated test function for get_module_import_string()
"""

import re
import pytest
from collections import OrderedDict
from src import unit_test_generator

# Now import modules specific to get_module_import_string:
from logging import Manager
from logging import PlaceHolder
from logging import StreamHandler
from logging import RootLogger
from logging import Logger
from pathlib import WindowsPath


# In sum, these tests covered 85.0% of get_module_import_string's lines
# Line(s) not covered by ANY of the tests below:
# ['619']
@pytest.mark.parametrize(
    "my_path, expected_result, args_after",
    [
        (
            WindowsPath(
                "ddt/tests/oo_car/car.py"
            ),
            "tests.oo_car.car",
            {
                "my_path": "WindowsPath('ddt/tests/oo_car/car.py')"
            },
        ),
    ],
)
def test_get_module_import_string(my_path, expected_result, args_after):
    """
    Programmatically generated test function for get_module_import_string()
    """
    result = unit_test_generator.get_module_import_string(my_path)
    assert result == expected_result
    assert my_path == eval(args_after["my_path"]) or args_after["my_path"] == my_path
