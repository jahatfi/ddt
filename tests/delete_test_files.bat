cd fizzbuzz
SET "keepfile=fizzbuzz.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd all_types
SET "keepfile=all_types.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd procedural_division
SET "keepfile=divide_ints.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd oo_car
SET "keepfile=car.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..

cd pass_by_assignment
SET "keepfile=pass_by_assignment.py"
FOR %%a IN (".\*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"
cd ..