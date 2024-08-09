"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1581', '1592', '1597-1598', '1606-1607', '1610-1611']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type, args_after",
    [
        (
            [1539, 1540, 1522, 1523, 1525, 1526, 1527],
            {1536, 1528, 1530, 1531, 1532, 1533, 1534, 1535},
            "['1539-1540', '1522-1523', '1525-1527']",
            list,
            {
                "this_list": "[1539, 1540, 1522, 1523, 1525, 1526, 1527]",
                "non_code_lines": "{1536, 1528, 1530, 1531, 1532, 1533, 1534, 1535}",
            },
        ),
    ],
)
def test_coverage_str_helper(
    this_list, non_code_lines, expected_result, expected_type, args_after
):
    """
    Programmatically generated test function for coverage_str_helper()
    """
    result = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
    assert args_after["this_list"] == this_list or this_list == eval(
        args_after["this_list"]
    )
    assert args_after["non_code_lines"] == non_code_lines or non_code_lines == eval(
        args_after["non_code_lines"]
    )
