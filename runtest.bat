@echo off
call venv\Scripts\activate

set "file="
set "tag="

:parse_args
if "%1"=="" goto execute
if "%1"=="--tags" (
    set "tag=%2"
    shift
) else (
    REM Si el archivo no comienza con features/, agregarlo
    set "file=%1"
    if not "%file:~0,9%"=="features/" (
        set "file=features/%1"
    )
)
shift
goto parse_args

:execute
if defined tag (
    if defined file (
        python -m pytest %file% -m %tag% --html=report.html
    ) else (
        python -m pytest -m %tag% --html=report.html
    )
) else (
    if defined file (
        python -m pytest %file% --html=report.html
    ) else (
        python -m pytest --html=report.html
    )
)

if %ERRORLEVEL% EQU 0 (
    echo Tests completados exitosamente!
    start report.html
) else (
    echo Algunos tests fallaron. Revisa el reporte...
    start report.html
) 