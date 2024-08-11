"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1670', '1675-1676', '1684-1685', '1688-1689', '1691']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1600, 1601, 1603, 1604, 1605, 1617, 1618],
            {1606, 1608, 1609, 1610, 1611, 1612, 1613, 1614},
            "['1600-1601', '1603-1605', '1617-1618']",
            {
                "this_list": "[1600, 1601, 1603, 1604, 1605, 1617, 1618]",
                "non_code_lines": "{1606, 1608, 1609, 1610, 1611, 1612, 1613, 1614}",
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
