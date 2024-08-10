"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 68.75% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1630', '1641', '1651-1653', '1655-1656', '1659-1660']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1282, 1283, 1284, 1285, 1286, 1287, 1288, 1295, 1296, 1258, 1270],
            {1280, 1278, 1260, 1268},
            "['1282-1288', '1295-1296', '1258']",
            {
                "this_list": "[1282, 1283, 1284, 1285, 1286, 1287, 1288, 1295, 1296, 1258, 1270]",
                "non_code_lines": "{1280, 1278, 1260, 1268}",
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
