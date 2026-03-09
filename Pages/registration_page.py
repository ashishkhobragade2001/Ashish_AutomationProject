from faker import Faker
from Locators.registration_locators import RegistrationLocators as RL
from Utilities.base_page import BasePage
from TestData.user_factory import UserFactory



class RegistrationPage(BasePage):

    def is_username_email_unique(self) -> bool:
        return self.is_element_visible(RL.ACCOUNT_CREATE_MESSAGE_TEXT, "account create message")

    def is_registration_successful(self) -> bool:
        return self.is_element_visible(RL.SUCCESSFUL_CREATE_MESSAGE_TEXT,
                                       "successful created message text")

    def new_user_signup(self, data: dict) -> None:
        # ------ for fake username an email address and others.
        self.log_info(f"\n============ start Registration ==================")

        # ------ for new sign in username and password
        self.click(RL.SIGNIN_TAB, locator_name="sign in tab")
        self.send_keys(RL.USERNAME_INPUT, data["signup_username"])
        self.send_keys(RL.EMAIL_INPUT, data["signup_email_address"])
        self.click(RL.SIGN_UP_BUTTON)

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
        self.click(RL.MR_TITLE_BUTTON, locator_name="MR_TITLE_BUTTON")
        self.send_keys(RL.PASSWORD_INPUT, data["password"], locator_name="password")
        self.scroll_to_element(RL.DAY_DROPDOWN, locator_name="dropdown days")
        self.select_by_value(RL.DAY_DROPDOWN, data["day"], locator_name="dropdown days")
        self.select_by_text(RL.MONTH_DROPDOWN, data["month"], locator_name=" DD month")
        self.select_by_value(RL.YEAR_DROPDOWN, data["year"], locator_name="DD year")

        self.click(RL.NEWS_LATTER_CHECKBOX, locator_name="news latter checkbox")
        self.click(RL.SPECIAL_OFFER_CHECKBOX, locator_name="special offer checkbox")

        self.scroll_to_element(RL.FIRST_NAME_INPUT, locator_name="first name input")
        self.send_keys(RL.FIRST_NAME_INPUT, data["first_name"], locator_name="first name ")
        self.send_keys(RL.LAST_NAME_INPUT, data["last_name"], "last name")
        self.send_keys(RL.COMPANY_INPUT, data["company"], "company ")
        self.send_keys(RL.ADDRESS_1_INPUT, data["address_1"], "address 1")
        self.send_keys(RL.ADDRESS_2_INPUT, data["address_2"], "address 2")
        self.send_keys(RL.ADDRESS_3_INPUT, data["address_3"], "address 3")

        self.scroll_to_element(RL.COUNTRY_DROPDOWN, "dropdown country")
        self.select_by_text(RL.COUNTRY_DROPDOWN, data["country_name"], "dropdown country")
        self.send_keys(RL.STATE_INPUT, data["state_name"], "state name")
        self.send_keys(RL.CITY_INPUT, data["city_name"], "city name")
        self.send_keys(RL.ZIPCODE_INPUT, data["zip_code"], "zip code")
        self.scroll_to_element(RL.MOBILE_NUMBER_INPUT, "mobile number")
        self.send_keys(RL.MOBILE_NUMBER_INPUT, data["mobile_number"], "mobile number")
        self.click(RL.CREATE_ACCOUNT_BUTTON, "create account button")
