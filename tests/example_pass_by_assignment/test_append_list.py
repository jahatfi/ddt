"""
Programmatically generated test function for append_list()
"""

import pytest
import pass_by_assignment


# In sum, these tests covered 100.0% of append_list's lines
@pytest.mark.parametrize(
    "this_list, item, expected_result, expected_type",
    [
        ([1, 2, 3, 4], 6, "None", "N/A"),
    ],
)
def test_append_list(this_list, item, expected_result, expected_type):
    """
    Programmatically generated test function for append_list()
    """
    result = pass_by_assignment.append_list(this_list, item)
    assert result == expected_result or result == eval(expected_result)
