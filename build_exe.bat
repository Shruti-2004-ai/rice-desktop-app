@echo off
setlocal

REM -------- user‑editable variables --------
set "MAIN=rice_app.py"
set "MODEL=rice_type_classifier.h5"
set "ASSET=samplecrop (1).jpeg"
REM -----------------------------------------

pip show pyinstaller >nul || pip install pyinstaller
if %errorlevel% neq 0 (
  echo PyInstaller install failed
  pause
  exit /b 1
)

echo Building %MAIN% …
pyinstaller --clean --noconfirm --onefile ^
  --add-data "%MODEL%;." ^
  --add-data "%ASSET%;." ^
  "%MAIN%"
if %errorlevel% neq 0 (
  echo Build failed.  See messages above.
  pause
  exit /b 1
)

echo Done!  Look inside dist\
pause
endlocal
