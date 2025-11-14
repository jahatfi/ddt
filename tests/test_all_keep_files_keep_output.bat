cd fizzbuzz
python fizzbuzz.py
coverage run -m pytest
::pytest -s -vv .
cd ..

cd all_types
python all_types.py
coverage run -m pytest
::pytest -s -vv .
cd ..

cd procedural_division
python divide_ints.py
coverage run -m pytest
::pytest -s -vv .
cd ..

cd oo_car
python example_car.py
coverage run -m pytest
::pytest -s -vv . 
cd ..

cd pass_by_assignment
python pass_by_assignment.py
pytest -s -vv . 
cd ..

cd ..\src
:: pytest .
coverage run -m pytest
cd ..

coverage combine tests\fizzbuzz\.coverage tests\oo_car\.coverage tests\all_types\.coverage tests\all_types\.coverage tests\procedural_division\.coverage src\.coverage
coverage report -m
coverage html