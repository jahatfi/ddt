cd fizzbuzz
python fizzbuzz.py
pytest -s -vv .
cd ..

cd all_types
python all_types.py
pytest -s -vv .
cd ..

cd procedural_division
python divide_ints.py
pytest -s -vv .
cd ..

cd oo_car
python car.py
pytest -s -vv . 
cd ..

cd pass_by_assignment
python pass_by_assignment.py
pytest -s -vv . 
cd ..

cd ..\src
pytest .
cd ..\tests

coverage combine tests\fizzbuzz\.coverage tests\oo_car\.coverage tests\all_types\.coverage tests\all_types\.coverage tests\procedural_division\.coverage src\.coverage
coverage report -m