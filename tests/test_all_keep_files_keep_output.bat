cd fizzbuzz
python fizzbuzz.py
pytest -s -v .
cd ..

cd all_types
python all_types.py
pytest -s -v .
cd ..

cd procedural_division
python divide_ints.py
pytest -s -v .
cd ..

cd oo_car
python car.py
pytest -s -v . 
cd ..

cd pass_by_assignment
python pass_by_assignment.py
pytest -s -v . 
cd ..