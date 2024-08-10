"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1629', '1640', '1645-1646', '1654-1655', '1658-1659']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1570, 1571, 1573, 1574, 1575, 1587, 1588],
            {1576, 1578, 1579, 1580, 1581, 1582, 1583, 1584},
            "['1570-1571', '1573-1575', '1587-1588']",
            {
                "this_list": "[1570, 1571, 1573, 1574, 1575, 1587, 1588]",
                "non_code_lines": "{1576, 1578, 1579, 1580, 1581, 1582, 1583, 1584}",
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
