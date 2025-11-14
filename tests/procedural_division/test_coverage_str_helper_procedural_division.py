"""
Programmatically generated test function for coverage_str_helper()
"""

import pytest
from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 71.88% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1806', '1817', '1822-1823', '1831-1832', '1835-1836']
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "this_list, non_code_lines, expected_result, args_after",
    [
        (
            [1764, 1765, 1747, 1748, 1750, 1751, 1752],
            {1760, 1761, 1753, 1755, 1756, 1757, 1758, 1759},
            "['1764-1765', '1747-1748', '1750-1752']",
            {
                "this_list": "[1764, 1765, 1747, 1748, 1750, 1751, 1752]",
                "non_code_lines": "{1760, 1761, 1753, 1755, 1756, 1757, 1758, 1759}",
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
    try:
        assert (
            this_list == eval(args_after["this_list"])
            or args_after["this_list"] == this_list
        )
        assert (
            non_code_lines == eval(args_after["non_code_lines"])
            or args_after["non_code_lines"] == non_code_lines
        )
    except KeyError as e:
        print(f"Got Key Error in test, likely false positive: {e=}")
