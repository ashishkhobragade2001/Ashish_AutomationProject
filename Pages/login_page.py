from Utilities.base_page import BasePage
from Locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def login(self, email: str, password: str) -> None:
        """
        Inserting the Right username and password to login field.
        :param email:
        :param password:
        :return: None
        """
        self.click(LoginLocators.LOGIN_BUTTON, "login button")
        self.send_keys(LoginLocators.EMAIL_INPUT, email, "email input")
        self.send_keys(LoginLocators.PASSWORD_INPUT, password, "password input")
        self.click(LoginLocators.SUBMIT_BUTTON, "submit button")

    def is_login_successful(self) -> bool:
        """
        after click on submit button validate login verification test isvisible or not.
        :return: return bool value if an element is visible.
        """
        return self.is_element_visible(LoginLocators.LOGIN_VRF_TEXT)
