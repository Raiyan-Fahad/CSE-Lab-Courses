@echo off
setlocal
where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed or not on PATH. Get it from https://www.python.org/downloads/
    exit /b 1
)
python "%~dp0zorvani_interpreter.py" %*
