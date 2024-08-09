cd example_fizzbuzz
SET "keepfile=fizzbuzz.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd example_all_types
SET "keepfile=all_types.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd example_procedural_division
SET "keepfile=divide_ints.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd example_oo_car
SET "keepfile=car.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd example_pass_by_assignment
SET "keepfile=pass_by_assignment.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..