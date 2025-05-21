from pages.login.login_locators import LoginPageLocators

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator(LoginPageLocators.USERNAME_INPUT)
        self.password_input = page.locator(LoginPageLocators.PASSWORD_INPUT)
        self.submit_button = page.locator(LoginPageLocators.SUBMIT_BUTTON)
        self.success_message = page.locator(LoginPageLocators.SUCCESS_MESSAGE)
        self.error_message = page.locator(LoginPageLocators.ERROR_MESSAGE)

    def navigate(self):
        """Navega a la página de login"""
        self.page.goto("https://practicetestautomation.com/practice-test-login/")
        self.page.wait_for_load_state("networkidle")

    def login(self, username, password):
        """Realiza el proceso de login con las credenciales proporcionadas"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
        
    def is_success_message_visible(self):
        """Verifica si el mensaje de éxito está visible"""
        return self.success_message.is_visible()
        
    def is_error_message_visible(self):
        """Verifica si el mensaje de error está visible"""
        return self.error_message.is_visible()
        
    def get_error_message(self):
        """Obtiene el texto del mensaje de error"""
        return self.error_message.text_content() if self.error_message.is_visible() else ""