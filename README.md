# Development Driven Testing, or "Self-Testing Code"

## Setup
Clone this repo to your local environment:  
`git clone $git_repo_url`  
Change directories into the newly cloned repo:  
`cd ddt`  
First initialize a Python virtual environment:  
`python -m venv venv`  
Activate the virtual environment:  
Windows Users:  
`.\venv\Scripts\activate.bat`  
Linux/Unix Users (Untested on Mac but should work):  
`source venv/bin/activate`
Install required packages:
`pip install -r requirements.txt`

**Note**:
You can exit your virtual environment easily once done:  
Windows Users:  
`.\venv\Scripts\deactivate.bat`  
Linux/Unix Users (Untested on Mac but should work):  
`deactivate`

## Runing the code

The easiest way to get started it to run one of the provided eamples.
Note that the various functions and methods in the example Python files 
are all decorated with the @unit_test_generator_decorator.  
\# TODO Decorate a class constructor!   
This is the decorator that enables automatic generation of unit tests.

Copy the unit_test_generator.py file straight into the example folders  
**\# (TODO: figure out the import issue to make this unnecessary)**  
`.\copy_unit_test_generator.bat` # Windows  
`./copy_unit_test_generator.sh`  # Linux, Unix, etc  

`cd` into the chosen example directory (e.g. example_oo_car, example_procedural_division, etc)
Run the code with Python, e.g.
    `python car.py` or
    `python divide_ints.py` or
    `python fizzbuzz.py`

Relevant files in directory of ..\ddt\example_oo_car **prior** to running `python car.py`:
```
| car.py                         # The orginal (untested) code that needs tests!
| unit_test_generator.py         # Local copy (copied with copy_unit_test_generator.{sh,bat})
```
Relevant files in directory of ..\ddt\example_oo_car **after** running `python car.py`:  
Note the **.json** and **test_*.py** files created after running the command above:
```
| Car.change_steer_angle.json    # Saved metadata for this decorated method
| Car.gas.json                   # Saved metadata for this decorated method
| car.py
| test_Car_change_steer_angle.py # Automatically generated unit test given car.py
| test_Car_gas.py                # Automatically generated unit test given car.py
| unit_test_generator.py
```
## Notes:
There is no need to monkey-unpatch (i.e. call `monkeypatch.delattr()`) variables after assertions to clean up the environment for the next function call, as every patchable variable on which a function depends is freshly patched before callling the function and asserting the results.
To demonstrate this idea, see these results from test_divideints.py:
```
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
I don't call need to call `monkeypatch.delattr("error_code")`, because I overwrite it with `setattr` before the next call.  EVERY global variable 
used by the tested function will be set before every call.


## Troubleshooting:
**Problem:** Decorator not running when expected  
**Solution:**  Check the cutoff parameter.  It might be to low for the desired executions to be hit.  Try setting it to 50 to start.


##  Paper TODO:

[] Prevent deadlocks by using a unique filename for each coverage or None to do it in memory (make this configurable)

[X] What if the decorated function throws an exception?  Catch all exceptions, save it, then re-raise it.  The test should assert the same exception is thrown.

[X] Methods differ from classes

Last: Update section references, e.g. "In sectionV/% I'll discuss..."

| Item         | Status (master) |
|--------------|-----------|
|test_auto_generate_tests.py||
|test_count_objects.py||
|test_coverage_str_helper.py||
|test_divide_ints.py||
|test_gen_coverage_list.py||
|test_meta_program_function_call.py||
|test_return_function_line_numbers_and_accessed_globals|Working|
