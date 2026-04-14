@echo off
REM Setup script for Windows
REM Systems Biology - Spatial Proteomics Course

echo =========================================
echo   Systems Biology Environment Setup
echo   Platform: Windows
echo =========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9 or higher and try again
    echo Download from: https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Run the Python setup script
echo Running setup script...
echo.

python setup_environment.py

REM Check if setup was successful
if %errorlevel% equ 0 (
    echo.
    echo =========================================
    echo   Setup completed successfully!
    echo =========================================
    echo.
    echo Next steps:
    echo   1. Activate the environment:
    echo      sysbio_env\Scripts\activate.bat
    echo.
    echo   2. Start Jupyter Notebook:
    echo      jupyter notebook
    echo.
) else (
    echo.
    echo =========================================
    echo   Setup completed with errors
    echo =========================================
    echo.
    echo Please check the error messages above and try again.
    pause
    exit /b 1
)

pause
