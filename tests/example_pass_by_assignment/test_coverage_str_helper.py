"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 78.12% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1481', '1492', '1506-1507', '1510-1511']
@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, expected_type",
    [
        (
            [1123, 1134, 1140, 1141, 1142, 1144, 1145, 1146],
            {1131, 1125},
            "['1123', '1134', '1140-1142', '1144-1146']",
            list,
        ),
    ],
)
def test_coverage_str_helper(this_list, non_code_lines, expected_result, expected_type):
    """
    Programmatically generated test function for coverage_str_helper()
    """
    result = unit_test_generator.coverage_str_helper(this_list, non_code_lines)
    assert isinstance(result, expected_type)
    assert result == expected_result or result == eval(expected_result)
