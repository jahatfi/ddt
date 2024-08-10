"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import Logger


# In sum, these tests covered 78.12% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1671-1672', '1675-1676', '1678', '1646']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1412, 1424, 1433, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1449, 1450],
            {1432, 1434, 1422, 1414},
            "['1412', '1424', '1433', '1436-1442', '1449-1450']",
            {
                "this_list": "[1412, 1424, 1433, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1449, 1450]",
                "non_code_lines": "{1432, 1434, 1422, 1414}",
            },
        ),
    ],
)
def test_coverage_str_helper(this_list, non_code_lines, expected_result, args_after):
    """
    Programmatically generated test function for coverage_str_helper()
    """
    result = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert result == expected_result or result == eval(expected_result)
    assert (
        this_list == eval(args_after["this_list"])
        or args_after["this_list"] == this_list
    )
    assert (
        non_code_lines == eval(args_after["non_code_lines"])
        or args_after["non_code_lines"] == non_code_lines
    )
