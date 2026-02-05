from selenium.webdriver.common.by import By

class RegistrationLocators:
    signin_tap = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
    name = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[3]/div[1]/form[1]/input[2]")
    email = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[3]/div[1]/form[1]/input[3]")
    signup_button = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[3]/div[1]/form[1]/button[1]")

    validation_text = (By.XPATH, "//b[text()='Enter Account Information']")
    mr_title = (By.ID, "id_gender1")
    password = (By.ID, "password")
    dropdown_days = (By.ID, "days")
    dropdown_months = (By.ID, "months")
    dropdown_years = (By.ID, "years")

    newsletter = (By.ID, "newsletter")
    special_offer = (By.XPATH, "//input[@id= 'optin']")

    # address informations locators
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

    varification_Logout_TAP = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
