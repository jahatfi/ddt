"""
Programmatically generated test function for coverage_str_helper
"""

from src import unit_test_generator

# Now import modules specific to coverage_str_helper:


# In sum, these tests covered 66.67% of coverage_str_helper's lines
# Line(s) not covered by ANY of the tests below:
# ['1439', '1450', '1461', '1471-1473', '1475-1476', '1479-1480']
def test_coverage_str_helper_0():
    """
    Programmatically generated test function for coverage_str_helper
    """
    # Coverage: 66.67% of function lines [1439-1484]
    # Covered Lines: 1448-1449;1451-1460;1462-1464;1466-1470;1478;1484
    # Lines not covered: 1439-1447;1450;1461;1471-1477;1479-1483
    # Note: Any lines not mentioned are comments or whitespace
    args = []
    args.append([1410, 1415, 1416, 1394, 1403])
    args.append(
        {1408, 1411, 1412, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1404, 1406, 1407}
    )
    x = unit_test_generator.coverage_str_helper(*args)
    assert x == ["1410", "1415-1416", "1394"]
