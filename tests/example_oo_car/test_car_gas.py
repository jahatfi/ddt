"""
Programmatically generated test function for Car.gas
"""

import re
import pytest
import car
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to Car.gas:
from car import Car


# In sum, these tests covered 85.71% of Car.gas's lines
# Line(s) not covered by ANY of the tests below:
# [58]
@pytest.mark.parametrize(
    "test_class_instance, rate, duration, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            Car("White", 12, -30),
            2,
            2,
            "N/A",
            "N/A",
            "16",
            int,
            {"method_call_counter": 1},
            {"method_call_counter": 2},
        ),
        (
            Car("Red", 10, 0),
            -1,
            1,
            ValueError,
            "Gas rate (m/s) must be positive.",
            "None",
            "N/A",
            {"method_call_counter": 0},
            {"method_call_counter": 1},
        ),
    ],
)
def test_car_gas(
    test_class_instance,
    rate,
    duration,
    exception_type,
    exception_message,
    result,
    return_type,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for Car.gas
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(car, k, v)
    if exception_type != "N/A":
        with pytest.raises(exception_type, match=re.escape(exception_message)):
            test_class_instance.gas(rate, duration)
    else:
        x = test_class_instance.gas(rate, duration)
        assert isinstance(x, return_type)
        assert (
            x == result or repr(x) == result or x == repr(result) or x == eval(result)
        )
    for global_var_written_to in ["method_call_counter"]:
        if global_var_written_to in ["None", "[]", "{}"]:
            assert not car.__dict__.get(global_var_written_to)
        else:
            assert (
                car.__dict__.get(global_var_written_to)
                == globals_after[global_var_written_to]
            )
