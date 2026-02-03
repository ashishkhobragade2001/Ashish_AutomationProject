from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN_BTN = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
    EMAIL = (By.XPATH, "//input[@data-qa='login-email']")
    PASSWORD = (By.XPATH, "//input[@data-qa='login-password']")
    SUBMIT = (By.XPATH, "//button[@data-qa='login-button']")
