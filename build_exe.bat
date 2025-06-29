@echo off
REM -----------------------------------------------------------
REM rice_app → standalone EXE
REM -----------------------------------------------------------
set "PYINSTALL=pyinstaller"
set "MAIN=rice_app.py"
set "MODEL=rice_type_classifier.h5"
set "ASSETS=samplecrop (1).jpg"

echo.
echo == Installing PyInstaller if missing...
pip show pyinstaller >nul || pip install pyinstaller

echo.
echo == Building one‑file executable...
%PYINSTALL% --clean --noconfirm --onefile ^
  --add-data "%MODEL%;." ^
  --add-data "%ASSETS%;." ^
  --hidden-import="numpy" ^
  --hidden-import="pillow" ^
  --hidden-import="streamlit" ^
  --hidden-import="tensorflow" ^
  --icon=NONE ^
  %MAIN%

echo.
echo == Build finished!
echo   Find rice_app.exe inside the "dist" folder.
pause
