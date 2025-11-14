"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1793', '1761', '1772', '1777-1778', '1786-1787', '1790-1791']
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1702, 1703, 1705, 1706, 1707, 1719, 1720],
            {1708, 1710, 1711, 1712, 1713, 1714, 1715, 1716},
            "['1702-1703', '1705-1707', '1719-1720']",
            {
                "this_list": "[1702, 1703, 1705, 1706, 1707, 1719, 1720]",
                "non_code_lines": "{1708, 1710, 1711, 1712, 1713, 1714, 1715, 1716}",
            },
        ),
    ],
    ids=counter,
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
