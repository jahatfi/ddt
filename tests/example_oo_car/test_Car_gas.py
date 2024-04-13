import car
import pytest
from _pytest.monkeypatch import MonkeyPatch

# Now import modules specific to Car.gas:
from car import Car


# In sum, these tests covered 57.14% of Car.gas's lines
# Line(s) not covered by ANY of the tests below:
# ['47', '57-58']
def test_Car_gas_0():
    monkeypatch = MonkeyPatch()

    # Coverage: 57.14% of function lines [47-58]
    # Covered Lines: 53-56
    # Lines not covered: 47-52;57-58
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
