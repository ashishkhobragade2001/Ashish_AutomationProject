from Utilities.base_page import BasePage
from Locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def login(self, email, password):
        self.click(LoginLocators.LOGIN_BTN)
        self.send_keys(LoginLocators.EMAIL, email)
        self.send_keys(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.SUBMIT)

    def is_login_successful(self):
        return self.is_element_visible(LoginLocators.LOGIN_VRF)
