"""
Programmatically generated test function for coverage_str_helper()
"""

import re
import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:
from logging import PlaceHolder
from logging import StreamHandler
from logging import Logger
from logging import Manager
from logging import RootLogger


# In sum, these tests covered 78.12% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1667', '1678', '1692-1693', '1696-1697']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1432, 1444, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1469, 1470],
            {1442, 1434, 1452, 1454},
            "['1432', '1444', '1456-1462', '1469-1470']",
            {
                "this_list": "[1432, 1444, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1469, 1470]",
                "non_code_lines": "{1442, 1434, 1452, 1454}",
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
