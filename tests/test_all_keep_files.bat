cd example_fizzbuzz
python fizzbuzz.py >NUL  2>NUL
pytest -s -v .
cd ..

cd example_all_types
python all_types.py >NUL  2>NUL
pytest -s -v .
cd ..

cd example_procedural_division
python divide_ints.py >NUL  2>NUL
pytest -s -v .
cd ..

cd example_oo_car
python car.py >NUL  2>NUL
pytest -s -v . 
cd ..

cd example_pass_by_assignment
python pass_by_assignment.py >NUL  2>NUL
pytest -s -v . 
cd ..