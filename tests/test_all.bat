cd example_fizzbuzz
python fizzbuzz.py >NUL  2>NUL
pytest -s -v .
@echo off
SET "keepfile=fizzbuzz.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
@echo on
cd ..

cd example_all_types
python all_types.py >NUL  2>NUL
pytest -s -v .
@echo off
SET "keepfile=all_types.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
@echo on
cd ..

cd example_procedural_division
python divide_ints.py >NUL  2>NUL
pytest -s -v .
@echo off
SET "keepfile=divide_ints.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
@echo on
cd ..

cd example_oo_car
python car.py >NUL  2>NUL
pytest -s -v . 
@echo off
SET "keepfile=car.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
@echo on
cd ..