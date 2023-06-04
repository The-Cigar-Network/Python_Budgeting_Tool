@echo off

echo Installing required packages...
pip install -r requirements.txt

echo Running the budgeting tool...
python main.py

echo Budgeting tool has exited.
pause
