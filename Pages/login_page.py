from Utilities.base_page import BasePage
from Locators.login_locators import LoginLocators

class LoginPage(BasePage):

    def open_login(self):
        self.click(LoginLocators.LOGIN_BTN)

    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL, email)
        self.send_keys(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.SUBMIT)
