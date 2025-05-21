@echo off
echo Agregando el directorio actual al PATH...
setx PATH "%PATH%;%CD%"
echo.
echo El directorio ha sido agregado al PATH.
echo Por favor, reinicia tu terminal para que los cambios surtan efecto.
echo.
pause 