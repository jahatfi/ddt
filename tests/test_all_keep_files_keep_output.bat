cd fizzbuzz
python example_fizzbuzz.py
coverage run -m pytest
::pytest -s -vv .
timeout 1
cd ..

cd all_types
python all_types.py
coverage run -m pytest
::pytest -s -vv .
cd ..

cd procedural_division
python example_divide_ints.py
coverage run -m pytest
::pytest -s -vv .
cd ..

cd oo_car
python example_car.py
coverage run -m pytest
::pytest -s -vv . 
cd ..

cd pass_by_assignment
python example_pass_by_assignment.py
coverage run -m pytest
cd ..

cd ..\src
:: pytest .
coverage run -m pytest
cd ..

: Give time for .coverage files to hit disk

coverage combine --keep tests\fizzbuzz\.coverage tests\oo_car\.coverage tests\all_types\.coverage tests\pass_by_assignment\.coverage tests\procedural_division\.coverage src\.coverage
coverage report -m
coverage html