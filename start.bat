@echo off
echo Installing requirements
timeout /t 5
pip install -r requirements.txt
python calc.py
