# language: en
Feature: Página principal
  Como visitante
  Quiero ver la página principal correctamente
  Para asegurarme de que la web está disponible

  Scenario: Verificar el título de la página principal
    Given que estoy en la página principal
    Then el título de la página debe ser "Practice Test Automation" 