from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-qa='login-password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_VRF_TEXT = (By.XPATH, "//li[contains(., ' Logged in as ')]")