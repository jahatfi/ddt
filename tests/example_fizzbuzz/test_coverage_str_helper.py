"""
Programmatically generated test function for coverage_str_helper
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 66.67% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1464', '1475', '1486', '1496-1498', '1500-1501', '1504-1505']
@pytest.mark.parametrize(
    "this_list, non_code_lines, result, return_type",
    [
        (
            [1412, 1413, 1415, 1416, 1429, 1430, 1433, 1403],
            {
                1408,
                1409,
                1410,
                1417,
                1419,
                1420,
                1421,
                1422,
                1423,
                1424,
                1425,
                1426,
                1431,
                1404,
                1405,
                1406,
                1407,
            },
            "['1412-1413', '1415-1416', '1429-1430', '1433']",
            list,
        ),
    ],
)
def test_coverage_str_helper(this_list, non_code_lines, result, return_type):
    """
    Programmatically generated test function for coverage_str_helper
    """
    x = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert isinstance(x, return_type)
    assert x == result or repr(x) == result or x == repr(result) or x == eval(result)
