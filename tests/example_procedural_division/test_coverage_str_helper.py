"""
Programmatically generated test function for coverage_str_helper
"""

from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 66.67% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1446', '1457', '1468', '1478-1480', '1482-1483', '1486-1487']
def test_coverage_str_helper_0():
    """
    Programmatically generated test function for coverage_str_helper
    """

    # Coverage: 66.67% of function lines [1446-1491]
    # Covered Lines: 1455-1456;1458-1467;1469-1471;1473-1477;1485;1491
    # Lines not covered: 1446-1454;1457;1468;1478-1484;1486-1490
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append([1409, 1414, 1415, 1393, 1402])
    args.append(
        {1410, 1411, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1403, 1405, 1406, 1407}
    )
    x = unit_test_generator.coverage_str_helper(*args)
    assert x == ["1409", "1414-1415", "1393"]
