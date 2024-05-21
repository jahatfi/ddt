"""
Programmatically generated test function for Car.gas
"""

import car
import pytest
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to Car.gas:
from car import Car


# In sum, these tests covered 85.71% of Car.gas's lines
# Line(s) not covered by ANY of the tests below:
# [58]
def test_car_gas_0():
    """
    Programmatically generated test function for Car.gas
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 57.14% of function lines [58-69]
    # Covered Lines: 64-67
    # Lines not covered: 58-63;68-69
    # Note: Any lines not mentioned are comments or whitespace
    method_call_counter = 0
    monkeypatch.setattr(car, "method_call_counter", method_call_counter)
    args = []
    args.append(-1)
    args.append(1)
    this_class = Car("Red", 10, 0)
    with pytest.raises(ValueError, match=r"Gas\ rate\ \(m/s\)\ must\ be\ positive\."):
        this_class.gas(*args)
    modified_method_call_counter = 1
    assert car.__dict__.get("method_call_counter") == modified_method_call_counter


def test_car_gas_1():
    """
    Programmatically generated test function for Car.gas
    """
    monkeypatch = MonkeyPatch()

    # Coverage: 71.43% of function lines [58-69]
    # Covered Lines: 64-66;68-69
    # Lines not covered: 58-63;67
    # Note: Any lines not mentioned are comments or whitespace
    method_call_counter = 1
    monkeypatch.setattr(car, "method_call_counter", method_call_counter)
    args = []
    args.append(2)
    args.append(2)
    this_class = Car("White", 12, -30)
    x = this_class.gas(*args)
    assert x == 16
    modified_method_call_counter = 2
    assert car.__dict__.get("method_call_counter") == modified_method_call_counter
