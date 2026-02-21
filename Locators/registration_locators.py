from selenium.webdriver.common.by import By


class RegistrationLocators:
    """
        Locators for Registration Flow.

        This class contains all web element locators related to:
        - User Log in
        - New user Registration
        -Logout

        These locators are used by the Registration class to perform
        user actions during automation of the New User Registration workflow.
        """
    # ---- sign in webpage
    SIGNIN_TAP = (By.XPATH, "//li[contains(., ' Signup / Login')]")
    USERNAME_INPUT = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGN_UP_BUTTON = (By.XPATH, "//button[@data-qa='signup-button']")

    # user information
    validation_text = (By.XPATH, "//b[text()='Enter Account Information']")
    MR_TITLE_BUTTON = (By.ID, "id_gender1")
    PASSWORD_INPUT = (By.ID, "password")
    DAY_DROPDOWN = (By.ID, "days")
    MONTH_DROPDOWN = (By.ID, "months")
    YEAR_DROPDOWN = (By.ID, "years")

    NEWS_LATTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFER_CHECKBOX = (By.XPATH, "//input[@id= 'optin']")

    # 🏗 address information locators
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS_1_INPUT = (By.XPATH, "(//input[@type= 'text'])[6]")
    ADDRESS_2_INPUT = (By.XPATH, "(//input[@type= 'text'])[7]")
    ADDRESS_3_INPUT = (By.XPATH, "(//input[@type= 'text'])[8]")

    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")

    SUCCESSFUL_CREATE_MESSAGE_TEXT = (By.XPATH, "//b[text()='Account Created!']")
    ACCOUNT_CREATE_MESSAGE_TEXT = (By.XPATH, "//b[contains(text(), 'Enter Account Information')]")

    CONTINUE_BUTTON = (By.XPATH, "//a[@class ='btn btn-primary']")
    LOGOUT_TAP = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
