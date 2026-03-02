from faker import Faker
from Locators.registration_locators import RegistrationLocators
from Utilities.base_page import BasePage
from TestData.user_factory import UserFactory




class RegistrationPage(BasePage):

    def is_username_email_unique(self) -> bool:
        return self.is_element_visible(RegistrationLocators.ACCOUNT_CREATE_MESSAGE_TEXT, "account create message")

    def is_registration_successful(self) -> bool:
        return self.is_element_visible(RegistrationLocators.SUCCESSFUL_CREATE_MESSAGE_TEXT, "successful created message text")

    def new_user_signup(self, data: dict) -> None:
        # ------ for fake username an email address and others.
        self.log_info(f"\n============ start Registration ==================")
        # fake = Faker("en_IN")
        # data["signup_username"] = fake.user_name() if data["signup_username"] else ""
        # data["signup_email_address"] = fake.email(domain="gmail.com") if data["signup_email_address"] else ""
        # data["password"] = fake.password() if data["password"] else ""
        # data["first_name"] = fake.first_name_male() if data["first_name"] else ""
        # data["last_name"] = fake.last_name() if data["last_name"] else ""
        # data["mobile_number"] = fake.numerify(text="9#########") if data["mobile_number"] else ""
        # data["company"] = fake.company()
        # data["address_1"] = fake.street_address()if data["address_1"] else ""
        # data["address_2"] = fake.street_name() + ", " + fake.city() if data["address_2"] else ""
        # data["state_name"] = fake.state() if data["state_name"] else ""
        # data["city_name"] = fake.city() if data["city_name"] else ""
        # data["zip_code"] = fake.zipcode_in_state(state_abbr="MH") if data["zip_code"] else ""
        #
        # self.log_info(f"username: {data["signup_username"]}")
        # self.log_info(f"signup_email_address: {data["signup_email_address"]}")

        # ------ for new sign in username and password
        self.click(RegistrationLocators.SIGNIN_TAB, locator_name="sign in tab")
        self.send_keys(RegistrationLocators.USERNAME_INPUT, data["signup_username"])
        self.send_keys(RegistrationLocators.EMAIL_INPUT, data["signup_email_address"])
        self.click(RegistrationLocators.SIGN_UP_BUTTON)

    def new_registration(self, data: dict) -> None:
        """
        A new username and email address for new user login. Get the data from Excel file having the following attribute
            signup_username: get username from faker module.
            signup_email_address: get email from faker module.
            password: get password from faker module.
            day: integer from 1 to 31
            month: month from January to December.
            year: get integer from excel file.
            First_name:first name of user.
            last_name: last name of user.
            company: company name of user.
            address_1: address of user having string max length 50.
            address_2: address of user having string max length 50.
            country_name: country name of user.
            state_name: state name of user.
            city_name: city name of user.
            zip_code: zip code in integer having max length 6 digit.
            Mobile_number: 10 digit integer.

        :param data: Read value from Excel.
        :return: True if expected equal to actual else False.
        """
        # ----- new registration details
        self.click(RegistrationLocators.MR_TITLE_BUTTON, locator_name="MR_TITLE_BUTTON")
        self.send_keys(RegistrationLocators.PASSWORD_INPUT, data["password"], locator_name="password")
        self.scroll_to_element(RegistrationLocators.DAY_DROPDOWN, locator_name="dropdown days")
        self.select_by_value(RegistrationLocators.DAY_DROPDOWN, data["day"], locator_name="dropdown days")
        self.select_by_text(RegistrationLocators.MONTH_DROPDOWN, data["month"], locator_name=" DD month")
        self.select_by_value(RegistrationLocators.YEAR_DROPDOWN, data["year"], locator_name="DD year")

        self.click(RegistrationLocators.NEWS_LATTER_CHECKBOX, locator_name="news latter checkbox")
        self.click(RegistrationLocators.SPECIAL_OFFER_CHECKBOX, locator_name="special offer checkbox")

        self.scroll_to_element(RegistrationLocators.FIRST_NAME_INPUT, locator_name="first name input")
        self.send_keys(RegistrationLocators.FIRST_NAME_INPUT, data["first_name"], locator_name="first name ")
        self.send_keys(RegistrationLocators.LAST_NAME_INPUT, data["last_name"], "last name")
        self.send_keys(RegistrationLocators.COMPANY_INPUT, data["company"], "company ")
        self.send_keys(RegistrationLocators.ADDRESS_1_INPUT, data["address_1"], "address 1")
        self.send_keys(RegistrationLocators.ADDRESS_2_INPUT, data["address_2"], "address 2")
        self.send_keys(RegistrationLocators.ADDRESS_3_INPUT, data["address_3"], "address 3")

        self.scroll_to_element(RegistrationLocators.COUNTRY_DROPDOWN, "dropdown country")
        self.select_by_text(RegistrationLocators.COUNTRY_DROPDOWN, data["country_name"], "dropdown country")
        self.send_keys(RegistrationLocators.STATE_INPUT, data["state_name"], "state name")
        self.send_keys(RegistrationLocators.CITY_INPUT, data["city_name"], "city name")
        self.send_keys(RegistrationLocators.ZIPCODE_INPUT, data["zip_code"], "zip code")
        self.scroll_to_element(RegistrationLocators.MOBILE_NUMBER_INPUT, "mobile number")
        self.send_keys(RegistrationLocators.MOBILE_NUMBER_INPUT, data["mobile_number"], "mobile number")
        self.click(RegistrationLocators.CREATE_ACCOUNT_BUTTON, "create account button")
