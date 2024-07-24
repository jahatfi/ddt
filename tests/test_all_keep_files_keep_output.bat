cd example_fizzbuzz
python fizzbuzz.py
pytest -s -v .
cd ..

cd example_all_types
python all_types.py
pytest -s -v .
cd ..

cd example_procedural_division
python divide_ints.py
pytest -s -v .
cd ..

cd example_oo_car
python car.py
pytest -s -v . 
cd ..

cd example_pass_by_assignment
python pass_by_assignment.py
pytest -s -v . 
cd ..