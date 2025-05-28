# language: es
Característica: Login en la aplicación
  Como usuario del sistema
  Quiero poder iniciar sesión
  Para acceder a mi cuenta

  Escenario: Login exitoso con credenciales válidas
    Dado que estoy en la página de login
    Cuando ingreso las credenciales
      | usuario | contraseña  |
      | student | Password123 |
    Y hago clic en el botón de login
    Entonces debería ver un mensaje de éxito

  Escenario: Login fallido con contraseña incorrecta
    Dado que estoy en la página de login
    Cuando ingreso las credenciales
      | usuario | contraseña         |
      | student | password_incorrecta|
    Y hago clic en el botón de login
    Entonces no debería ver un mensaje de éxito

  Escenario: Login fallido con usuario inválido
    Dado que estoy en la página de login
    Cuando ingreso las credenciales
      | usuario         | contraseña  |
      | usuario_invalido| Password123 |
    Y hago clic en el botón de login
    Entonces no debería ver un mensaje de éxito 