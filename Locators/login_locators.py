from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_BTN = (By.XPATH, "//a[contains(text(), ' Signup / Login')]")
    EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    SUBMIT = (By.XPATH, "//button[@data-qa='login-button']")
    LOGIN_VRF = (By.XPATH, "//li[contains(., ' Logged in as ')]")