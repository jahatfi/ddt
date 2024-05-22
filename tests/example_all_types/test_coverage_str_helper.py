"""
Programmatically generated test function for coverage_str_helper
"""

from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 66.67% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1445', '1456', '1467', '1477-1479', '1481-1482', '1485-1486']
def test_coverage_str_helper_0():
    """
    Programmatically generated test function for coverage_str_helper
    """

    # Coverage: 66.67% of function lines [1445-1490]
    # Covered Lines: 1454-1455;1457-1466;1468-1470;1472-1476;1484;1490
    # Lines not covered: 1445-1453;1456;1467;1477-1483;1485-1489
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append([1408, 1411, 1412, 1413, 1414, 1415, 1392, 1400, 1401, 1403, 1407])
    args.append(
        {1409, 1410, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1402, 1404, 1405, 1406}
    )
    x = unit_test_generator.coverage_str_helper(*args)
    assert x == ["1408", "1411-1415", "1392", "1400-1401", "1403"]
