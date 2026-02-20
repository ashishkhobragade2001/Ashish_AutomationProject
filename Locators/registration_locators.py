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
    signin_tap = (By.XPATH, "//li[contains(., ' Signup / Login')]")
    name = (By.XPATH, "//input[@data-qa='signup-name']")
    email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")

    # user information
    validation_text = (By.XPATH, "//b[text()='Enter Account Information']")
    mr_title = (By.ID, "id_gender1")
    password = (By.ID, "password")
    dropdown_days = (By.ID, "days")
    dropdown_months = (By.ID, "months")
    dropdown_years = (By.ID, "years")

    newsletter = (By.ID, "newsletter")
    special_offer = (By.XPATH, "//input[@id= 'optin']")

    # 🏗 address information locators
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    company = (By.ID, "company")
    address_1 = (By.XPATH, "(//input[@type= 'text'])[6]")
    address_2 = (By.XPATH, "(//input[@type= 'text'])[7]")
    address_3 = (By.XPATH, "(//input[@type= 'text'])[8]")

    dropdown_country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile_number = (By.ID, "mobile_number")
    create_account_button = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")

    successfully_create_message = (By.XPATH, "//b[text()='Account Created!']")
    continue_button = (By.XPATH, "//a[@class ='btn btn-primary']")

    verification_Logout_TAP = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
