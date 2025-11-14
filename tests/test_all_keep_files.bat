cd fizzbuzz
python example_fizzbuzz.py >NUL  2>NUL
pytest -s -vv .
cd ..

cd all_types
python all_types.py >NUL  2>NUL
pytest -s -vv .
cd ..

cd procedural_division
python example_divide_ints.py >NUL  2>NUL
pytest -s -vv .
cd ..

cd oo_car
python example_car.py >NUL  2>NUL
pytest -s -vv . 
cd ..

cd pass_by_assignment
python example_pass_by_assignment.py >NUL  2>NUL
pytest -s -vv . 
cd ..