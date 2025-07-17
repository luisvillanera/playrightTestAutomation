# language: en
Feature: Login en la aplicación
  Como usuario del sistema
  Quiero poder iniciar sesión
  Para acceder a mi cuenta

  Scenario: Login exitoso con credenciales válidas
    Given que estoy en la página de login
    When ingreso las credenciales
      | usuario | contraseña  |
      | student | Password123 |
    And hago clic en el botón de login
    Then debería ver un mensaje de éxito

  Scenario: Login fallido con contraseña incorrecta
    Given que estoy en la página de login
    When ingreso las credenciales
      | usuario | contraseña         |
      | student | password_incorrecta|
    And hago clic en el botón de login
    Then no debería ver un mensaje de éxito

  Scenario: Login fallido con usuario inválido
    Given que estoy en la página de login
    When ingreso las credenciales
      | usuario         | contraseña  |
      | usuario_invalido| Password123 |
    And hago clic en el botón de login
    Then no debería ver un mensaje de éxito 