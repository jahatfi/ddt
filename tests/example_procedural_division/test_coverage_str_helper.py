"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1586', '1597', '1602-1603', '1611-1612', '1615-1616']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type, args_after",
    [
        (
            [1544, 1545, 1527, 1528, 1530, 1531, 1532],
            {1536, 1537, 1538, 1539, 1540, 1541, 1533, 1535},
            "['1544-1545', '1527-1528', '1530-1532']",
            list,
            {
                "this_list": "[1544, 1545, 1527, 1528, 1530, 1531, 1532]",
                "non_code_lines": "{1536, 1537, 1538, 1539, 1540, 1541, 1533, 1535}",
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
    assert (
        this_list == eval(args_after["this_list"])
        or args_after["this_list"] == this_list
    )
    assert (
        non_code_lines == eval(args_after["non_code_lines"])
        or args_after["non_code_lines"] == non_code_lines
    )
