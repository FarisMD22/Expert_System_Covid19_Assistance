@echo off
REM CIDAS Installation Script for Windows
REM Handles Python 3.10+ compatibility automatically

echo ============================================================
echo CIDAS - COVID-19 Expert System Installation
echo ============================================================
echo.
echo Python 3.12 detected - compatibility patch embedded in code
echo.
echo Installing dependencies...
echo.

REM Install packages one by one to avoid conflicts
pip install experta
pip install scikit-fuzzy
pip install "numpy<2.0"
pip install streamlit
pip install pandas
pip install plotly
pip install matplotlib

echo.
echo ============================================================
echo Installation Complete!
echo ============================================================
echo.
echo Testing installation...
echo.

REM Test facts.py (now has built-in compatibility patch)
python facts.py

echo.
echo ============================================================
echo Testing Complete!
echo ============================================================
echo.

pause