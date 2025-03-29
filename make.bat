@echo off
IF %1.==. GOTO commad_missing
IF %1 == install GOTO install
IF %1 == build GOTO build
IF %1 == push GOTO push
	ECHO Undefined command
GOTO End1

:commad_missing
  ECHO Command is missing
  GOTO End1

:install
  ECHO Installing package...
  pip install -e . --upgrade --upgrade-strategy only-if-needed
  GOTO End1

:build
  ECHO Building package...
  python -m pip install --upgrade build
  python -m build
  GOTO End1

:push
	python -m pip install --upgrade twine
	python -m pip install -U packaging
	python -m twine upload dist/*

:End1