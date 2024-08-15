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