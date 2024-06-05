"""
Programmatically generated test function for coverage_str_helper
"""

from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 75.76% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1451', '1462', '1473', '1487-1488', '1491-1492']
def test_coverage_str_helper_0():
    """
    Programmatically generated test function for coverage_str_helper
    """

    # Coverage: 75.76% of function lines [1451-1496]
    # Covered Lines: 1460-1461;1463-1472;1474-1476;1478-1485;1490;1496
    # Lines not covered: 1451-1459;1462;1473;1487-1489;1491-1495
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append([1409, 1413, 1414, 1417, 1418, 1419, 1420, 1421, 1398, 1406, 1407])
    args.append(
        {1408, 1410, 1411, 1412, 1415, 1416, 1399, 1400, 1401, 1402, 1403, 1404, 1405}
    )
    x = unit_test_generator.coverage_str_helper(*args)
    assert x == ["1409", "1413-1414", "1417-1421", "1398", "1406-1407"]
