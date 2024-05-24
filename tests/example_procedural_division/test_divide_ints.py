"""
Programmatically generated test function for divide_ints
"""

import pytest
import divide_ints
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to divide_ints:

ERROR_CODE = 0


# In sum, these tests covered 91.67% of divide_ints's lines
# Line(s) not covered by ANY of the tests below:
# [26]
@pytest.mark.parametrize(
    "a,b, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            6,
            2,
            "N/A",
            "N/A",
            "N/A",
            "6/2=3.0",
            "str",
            {"error_code": "0"},
            {"error_code": "0"},
        ),
        (
            3,
            0,
            "N/A",
            "<class 'ValueError'>",
            "ValueError: Cannot divide by zero!",
            "None",
            "N/A",
            {"error_code": "0"},
            {"error_code": "-3"},
        ),
        (
            "10",
            2,
            "N/A",
            "<class 'TypeError'>",
            "TypeError: Variable a='10' is not an int!",
            "None",
            "N/A",
            {"error_code": "0"},
            {"error_code": "-1"},
        ),
        (
            8,
            [],
            "N/A",
            "<class 'TypeError'>",
            "TypeError: Variable b=[] is not an int!",
            "None",
            "N/A",
            {"error_code": "0"},
            {"error_code": "-2"},
        ),
    ],
)
def test_divide_ints(
    a,
    b,
    kwargs,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for divide_ints
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(divide_ints, "error_code", ERROR_CODE)
    x = divide_ints.divide_ints(a, b)
    assert x == result or repr(x) == result or repr(result) == x
    for global_var_written_to in ["error_code"]:
        if global_var_written_to in ["None", "[]", "{}"]:
            assert not divide_ints.__dict__.get(global_var_written_to)
        else:
            assert (
                divide_ints.__dict__.get(global_var_written_to) == global_var_written_to
            )
