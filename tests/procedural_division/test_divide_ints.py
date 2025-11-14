"""
Programmatically generated test function for divide_ints()
"""

import re
import pytest
import divide_ints
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to divide_ints:


# In sum, these tests covered 100.0% of divide_ints's lines
def counter(start=0) -> str:
    while True:
        yield f"test#-{start}"
        start += 1


@pytest.mark.parametrize(
    "a, b, exception_type, exception_message, expected_result, args_after, globals_before, globals_after",
    [
        (
            8,
            [],
            TypeError,
            "TypeError: Variable b=[] is not an int!",
            "None",
            {"b": "[]"},
            {"error_code": -1},
            {"error_code": -2},
        ),
        (
            "10",
            2,
            TypeError,
            "TypeError: Variable a='10' is not an int!",
            "None",
            {},
            {"error_code": -3},
            {"error_code": -1},
        ),
        (
            3,
            0,
            ValueError,
            "ValueError: Cannot divide by zero!",
            "None",
            {},
            {"error_code": 0},
            {"error_code": -3},
        ),
        (6, 2, "N/A", "N/A", "6/2=3.0", {}, {"error_code": 0}, {"error_code": 0}),
    ],
    ids=counter,
)
def test_divide_ints(
    a,
    b,
    exception_type,
    exception_message,
    expected_result,
    args_after,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for divide_ints()
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(divide_ints, k, v)
    if exception_type != "N/A":
        with pytest.raises(exception_type, match=re.escape(exception_message)):
            divide_ints.divide_ints(a, b)
    else:
        result = divide_ints.divide_ints(a, b)
        assert result == expected_result or result == eval(expected_result)
        try:
            assert b == eval(args_after["b"]) or args_after["b"] == b
        except KeyError as e:
            print(f"Got Key Error in test, likely false positive: {e=}")
    for global_var_written_to in ["error_code"]:
        if global_var_written_to in ["None", "[]", "{}"]:
            assert not divide_ints.__dict__.get(global_var_written_to)
        else:
            assert (
                divide_ints.__dict__.get(global_var_written_to)
                == globals_after[global_var_written_to]
            )
