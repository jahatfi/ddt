"""
Programmatically generated test function for divide_ints
"""

import divide_ints
import pytest
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to divide_ints:

ERROR_CODE = 0


# In sum, these tests covered 91.67% of divide_ints's lines
# Line(s) not covered by ANY of the tests below:
# [26]
def test_divide_ints_0():
    """
    Programmatically generated test function for divide_ints
    """
    monkeypatch = MonkeyPatch()

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


def test_divide_ints_1():
    """
    Programmatically generated test function for divide_ints
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 50.00% of function lines [26-42]
    # Covered Lines: 32-33;36;39-41
    # Lines not covered: 26-31;34-35;37-38;42
    # Note: Any lines not mentioned are comments or whitespace
    monkeypatch.setattr(divide_ints, "error_code", ERROR_CODE)
    args = []
    args.append(3)
    args.append(0)
    with pytest.raises(ValueError, match=r"ValueError:\ Cannot\ divide\ by\ zero!"):
        divide_ints.divide_ints(*args)
    modified_error_code = -3
    assert divide_ints.__dict__.get("error_code") == modified_error_code


def test_divide_ints_2():
    """
    Programmatically generated test function for divide_ints
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 33.33% of function lines [26-42]
    # Covered Lines: 32-35
    # Lines not covered: 26-31;36-42
    # Note: Any lines not mentioned are comments or whitespace
    monkeypatch.setattr(divide_ints, "error_code", ERROR_CODE)
    args = []
    args.append("10")
    args.append(2)
    with pytest.raises(
        TypeError, match=r"TypeError:\ Variable\ a='10'\ is\ not\ an\ int!"
    ):
        divide_ints.divide_ints(*args)
    modified_error_code = -1
    assert divide_ints.__dict__.get("error_code") == modified_error_code


def test_divide_ints_3():
    """
    Programmatically generated test function for divide_ints
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 41.67% of function lines [26-42]
    # Covered Lines: 32-33;36-38
    # Lines not covered: 26-31;34-35;39-42
    # Note: Any lines not mentioned are comments or whitespace
    monkeypatch.setattr(divide_ints, "error_code", ERROR_CODE)
    args = []
    args.append(8)
    args.append([])
    with pytest.raises(
        TypeError, match=r"TypeError:\ Variable\ b=\[\]\ is\ not\ an\ int!"
    ):
        divide_ints.divide_ints(*args)
    modified_error_code = -2
    assert divide_ints.__dict__.get("error_code") == modified_error_code
