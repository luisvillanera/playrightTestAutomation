import pytest
from pages.login.login_page import LoginPage


def test_login_valid(page):
    """Test de login exitoso - escenario smoke"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("student", "Password123")
    
    # Verificar que el mensaje de éxito sea visible
    assert login_page.is_success_message_visible(), "El mensaje de éxito no está visible"

def test_login_invalid_password(page):
    """Test de login con contraseña inválida"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("student", "password_incorrecta")
    assert not login_page.is_success_message_visible(), "No debería mostrarse el mensaje de éxito"

def test_login_invalid_user(page):
    """Test de login con usuario inválido"""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("usuario_invalido", "Password123")
    assert not login_page.is_success_message_visible(), "No debería mostrarse el mensaje de éxito"