@echo off
set inSource=%1
set source=%inSource%

IF "%source%" == "" (
	set source=.
)

echo AwareLibrary Source: %source%

set mypath=%cd%
cd %source%

rd /S /Q AwareLibrarySetup\build
rd /S /Q AwareLibrarySetup\wheel

cd AwareLibrarySetup
python.exe setup.py bdist_wheel -d wheel

cd wheel

FOR %%G IN (*.whl) do (pip.exe install --upgrade "%%G")

cd %mypath%
set doc=%source%\AwareLibrarySetup\docs

IF "%inSource%" == "" (
	IF exist %doc% ( echo %doc% ) ELSE ( md %doc% && echo %doc% created)

	REM genarate libdoc
	python.exe -m robot.libdoc AwareLibrary %doc%\AwareLibrary.html

	timeout 10
)