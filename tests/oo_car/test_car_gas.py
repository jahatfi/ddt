"""
Programmatically generated test function for Car.gas()
"""

import re
import pytest
from collections import OrderedDict
from tests.oo_car import car
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to Car.gas:
from logging import Logger
from logging import Manager
from logging import PlaceHolder
from logging import RootLogger
from logging import StreamHandler
from tests.oo_car.car import Car


# In sum, these tests covered 100.0% of Car.gas's lines
@pytest.mark.parametrize(
    "test_class_instance, rate, duration, exception_type, exception_message, expected_result, globals_before, globals_after",
    [
        (
            Car("Red", 10, 0),
            -1,
            1,
            ValueError,
            "Gas rate (m/s) must be positive.",
            "None",
            {"method_call_counter": 0},
            {"method_call_counter": 1},
        ),
        (
            Car("White", 12, -30),
            2,
            2,
            "N/A",
            "N/A",
            "16",
            {"method_call_counter": 1},
            {"method_call_counter": 2},
        ),
    ],
)
def test_car_gas(
    test_class_instance,
    rate,
    duration,
    exception_type,
    exception_message,
    expected_result,
    globals_before,
    globals_after,
):
    """
    Programmatically generated test function for Car.gas()
    """
    monkeypatch = MonkeyPatch()
    for k, v in globals_before.items():
        monkeypatch.setattr(car, k, v)
    if exception_type != "N/A":
        with pytest.raises(exception_type, match=re.escape(exception_message)):
            test_class_instance.gas(rate, duration)
    else:
        result = test_class_instance.gas(rate, duration)
        assert result == expected_result or result == eval(expected_result)
    for global_var_written_to in ["method_call_counter"]:
        if global_var_written_to in ["None", "[]", "{}"]:
            assert not car.__dict__.get(global_var_written_to)
        else:
            assert (
                car.__dict__.get(global_var_written_to)
                == globals_after[global_var_written_to]
            )
