"""
Programmatically generated test function for divide_ints
"""

import divide_ints
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to divide_ints:

ERROR_CODE = 0


# In sum, these tests covered 41.67% of divide_ints's lines
# Line(s) not covered by ANY of the tests below:
# ['34-35', '37-38', '40-41']
def test_divide_ints_0():
    monkeypatch = MonkeyPatch()
    """
    Programmatically generated test function for divide_ints
    """
    # Coverage: 41.67% of function lines [26-42]
    # Covered Lines: 32-33;36;39;42
    # Lines not covered: 26-31;34-35;37-38;40-41
    # Note: Any lines not mentioned are comments or whitespace
    monkeypatch.setattr(divide_ints, "error_code", ERROR_CODE)
    args = []
    args.append(6)
    args.append(2)
    x = divide_ints.divide_ints(*args)
    assert x == "6/2=3.0"
    modified_error_code = 0
    assert divide_ints.__dict__.get("error_code") == modified_error_code
