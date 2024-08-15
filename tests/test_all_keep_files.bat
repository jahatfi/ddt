cd fizzbuzz
python fizzbuzz.py >NUL  2>NUL
pytest -s -vv .
cd ..

cd all_types
python all_types.py >NUL  2>NUL
pytest -s -vv .
cd ..

cd procedural_division
python divide_ints.py >NUL  2>NUL
pytest -s -vv .
cd ..

cd oo_car
python car.py >NUL  2>NUL
pytest -s -vv . 
cd ..

cd pass_by_assignment
python pass_by_assignment.py >NUL  2>NUL
pytest -s -vv . 
cd ..