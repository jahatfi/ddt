![CI](https://github.com/jahatfi/ddt/actions/workflows/python-app-ubuntu.yml/badge.svg)
![CI](https://github.com/jahatfi/ddt/actions/workflows/python-app-windows.yml/badge.svg)

# Please read the paper (ddt_paper.pdf) included herein.

Notes:

Need to test coverage with non-standard types, e.g. default dictionary 
Some of the asserts may be superfluous.  I intentionally assert that all modified objects are modified as expected, as "pass by assignment" means
that any argument passed in may be used by the calling function, so assert it was (or wasn't) modified as expected.

# Development Driven Testing, or "Self-Testing Code"

## Setup
Use poetry, e.g. 

`poetry init && poetry install && poetry shell`  

**Note**:
You can exit your virtual environment easily once done:  
Windows Users:  
`.\venv\Scripts\deactivate.bat`  
Linux/Unix Users (Untested on Mac but should work):  
`deactivate`

## Running the code

The easiest way to get started is to run one of the provided examples.
Note that the various functions and methods in the example Python files 
are all decorated with `@unit_test_generator_decorator`.

This is the decorator that enables automatic generation of unit tests.

`cd` into the chosen example directory (e.g. tests/example_all_types/) 
(more examples to come)  
Run the code with Python, e.g.  
    `python all_types.py` or 
    `python car.py` or 
    `python divide_ints.py` or 
    `python fizzbuzz.py`

Relevant files in directory of ..\ddt\example_oo_car **prior** 
to running `python car.py`:
```python
| car.py                  # The orginal (untested) code that needs tests!
```
Relevant files in directory of ..\ddt\example_oo_car **after** running `python car.py`:  
Note the **.json** and **test_*.py** files created after running the command above:
```python
| Car.change_steer_angle.json    # Saved metadata for this decorated method
| Car.gas.json                   # Saved metadata for this decorated method
| car.py
| test_Car_change_steer_angle.py # Automatically generated unit test given car.py
| test_Car_gas.py                # Automatically generated unit test given car.py
```
## Notes:
There is no need to monkey-unpatch (i.e. call `monkeypatch.delattr()`) 
variables after assertions to clean up the environment for the next 
function call, as every patchable variable on which a function 
depends is freshly patched before calling the function and 
asserting the results.
To demonstrate this idea, see these results from test_divide_ints.py:

```python
    # Coverage: 45.45% of function lines [17-27]
    # Covered Lines: 17-18;21;24;27
    # Lines not covered: 19-20;22-23;25-26
    # Note: Any lines not mentioned are comments or whitespace
    error_code = 0
    monkeypatch.setattr(divide_ints, "error_code", error_code)
    args = []
    args.append(6)
    args.append(2)
    x = divide_ints.divide_ints(*args)
    assert x == "6/2=3.0"
    error_code_modified = 0
    assert divide_ints.__dict__.get("error_code") == error_code_modified

    # Coverage: 54.55% of function lines [17-27]
    # Covered Lines: 17-18;21;24-26
    # Lines not covered: 19-20;22-23;27
    # Note: Any lines not mentioned are comments or whitespace
    error_code = 0
    monkeypatch.setattr(divide_ints, "error_code", error_code)
    args = []
    args.append(3)
    args.append(0)
    with pytest.raises(ValueError, match=r"ValueError:\ Cannot\ divide\ by\ zero!"):
        divide_ints.divide_ints(*args)
    error_code_modified = -3
    assert divide_ints.__dict__.get("error_code") == error_code_modified
```
I don't call need to call `monkeypatch.delattr("error_code")`, 
because I overwrite it with `setattr` before the next call.  EVERY global variable 
used by the tested function will be set before every call.

## Troubleshooting:
**Problem:** Decorator not running when expected  
**Solution:**  Check the cutoff parameter.
It might be too low for the desired executions to be hit.
Try setting it to 50 to start.
