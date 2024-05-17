"""
Programmatically generated test function for coverage_str_helper
"""

from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 75.76% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1434', '1445', '1456', '1470-1471', '1474-1475']
def test_coverage_str_helper_0():
    """
    Programmatically generated test function for coverage_str_helper
    """
    # Coverage: 75.76% of function lines [1434-1479]
    # Covered Lines: 1443-1444;1446-1455;1457-1459;1461-1468;1473;1479
    # Lines not covered: 1434-1442;1445;1456;1470-1472;1474-1478
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append([1408, 1409, 1410, 1411, 1412, 1389, 1397, 1398, 1400, 1404, 1405])
    args.append(
        {1390, 1391, 1392, 1393, 1394, 1395, 1396, 1399, 1401, 1402, 1403, 1406, 1407}
    )
    x = unit_test_generator.coverage_str_helper(*args)
    assert x == ["1408-1412", "1389", "1397-1398", "1400", "1404-1405"]
