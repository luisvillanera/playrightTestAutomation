@echo off
call venv\Scripts\activate

echo Ordenando imports...
isort .

echo.
echo Formateando código...
black .

echo.
echo ¡Código formateado exitosamente!
pause 