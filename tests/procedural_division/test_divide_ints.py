"""
Programmatically generated test function for divide_ints()
"""

import re
import pytest
from collections import OrderedDict
import divide_ints
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to divide_ints:
from logging import StreamHandler
from logging import Manager
from logging import Logger
from logging import PlaceHolder
from logging import RootLogger

ERROR_CODE = 0


# In sum, these tests covered 100.0% of divide_ints's lines
@pytest.mark.parametrize(
    "a, b, exception_type, exception_message, expected_result, args_after, globals_before, globals_after",
    [
        (
            "10",
            2,
            TypeError,
            "TypeError: Variable a='10' is not an int!",
            "None",
            {"a": '"10"', "b": "2"},
            {},
            {"error_code": -1},
        ),
        (
            8,
            [],
            TypeError,
            "TypeError: Variable b=[] is not an int!",
            "None",
            {"a": "8", "b": "[]"},
            {},
            {"error_code": -2},
        ),
        (6, 2, "N/A", "N/A", "6/2=3.0", {"a": "6", "b": "2"}, {}, {"error_code": 0}),
        (
            3,
            0,
            ValueError,
            "ValueError: Cannot divide by zero!",
            "None",
            {"a": "3", "b": "0"},
            {},
            {"error_code": -3},
        ),
    ],
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
    monkeypatch.setattr(divide_ints, "error_code", ERROR_CODE)
    if exception_type != "N/A":
        with pytest.raises(exception_type, match=re.escape(exception_message)):
            divide_ints.divide_ints(a, b)
    else:
        result = divide_ints.divide_ints(a, b)
        assert result == expected_result or result == eval(expected_result)
        assert a == eval(args_after["a"]) or args_after["a"] == a
        assert b == eval(args_after["b"]) or args_after["b"] == b
    for global_var_written_to in ["error_code"]:
        if global_var_written_to in ["None", "[]", "{}"]:
            assert not divide_ints.__dict__.get(global_var_written_to)
        else:
            assert (
                divide_ints.__dict__.get(global_var_written_to)
                == globals_after[global_var_written_to]
            )
