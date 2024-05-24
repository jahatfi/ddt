"""
Programmatically generated test function for coverage_str_helper
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 66.67% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1446', '1457', '1468', '1478-1480', '1482-1483', '1486-1487']
@pytest.mark.parametrize(
    "this_list,non_code_lines, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            [1409, 1414, 1415, 1393, 1402],
            {
                1410,
                1411,
                1394,
                1395,
                1396,
                1397,
                1398,
                1399,
                1400,
                1403,
                1405,
                1406,
                1407,
            },
            "N/A",
            "N/A",
            "N/A",
            "['1409', '1414-1415', '1393']",
            "list",
            {},
            {},
        ),
    ],
)
def test_coverage_str_helper(
    this_list,
    non_code_lines,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for coverage_str_helper
    """
    x = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert x == result or repr(x) == result or repr(result) == x
