"""
Programmatically generated test function for Car.gas
"""

import pytest
import car
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to Car.gas:
from car import Car


# In sum, these tests covered 85.71% of Car.gas's lines
# Line(s) not covered by ANY of the tests below:
# [58]
@pytest.mark.parametrize(
    "self,rate,duration, kwargs, exception_type, exception_message, result, return_type, globals_before, globals_after",
    [
        (
            -1,
            1,
            "N/A",
            "<class 'ValueError'>",
            "Gas rate (m/s) must be positive.",
            "None",
            "N/A",
            {"method_call_counter": "0"},
            {"method_call_counter": "1"},
        ),
        (
            2,
            2,
            "N/A",
            "N/A",
            "N/A",
            "16",
            "int",
            {"method_call_counter": "1"},
            {"method_call_counter": "2"},
        ),
    ],
)
def test_car_gas(
    self,
    rate,
    duration,
    kwargs,
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
    this_class = Car("Red", 10, 0)
    with pytest.raises(ValueError, match=r"Gas\ rate\ \(m/s\)\ must\ be\ positive\."):
        this_class.gas(self, rate, duration)
    for global_var_written_to in ["method_call_counter"]:
        if global_var_written_to in ["None", "[]", "{}"]:
            assert not car.__dict__.get(global_var_written_to)
        else:
            assert car.__dict__.get(global_var_written_to) == global_var_written_to
