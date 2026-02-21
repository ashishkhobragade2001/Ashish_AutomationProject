from faker import Faker
from Locators.registration_locators import RegistrationLocators
from Utilities.base_page import BasePage


class RegistrationPage(BasePage):

    def is_username_email_unique(self):
        return self.is_element_visible(RegistrationLocators.ACCOUNT_CREATE_MESSAGE_TEXT)

    def is_registration_successful(self):
        return self.is_element_visible(RegistrationLocators.SUCCESSFUL_CREATE_MESSAGE_TEXT)

    def new_user_signup(self, data):
        # ------ for fake username an EMAIL_INPUT address
        fake = Faker()
        data["signup_username"] = fake.user_name()
        data["signup_email_address"] = fake.email(domain="outlook")
        self.log_info(f"username: {data["signup_username"]}")
        self.log_info(f"signup_email_address: {data["signup_email_address"]}")

        # ------ for new sign in username and password
        self.click(RegistrationLocators.SIGNIN_TAP, locator_name="sign in tab")
        self.send_keys(RegistrationLocators.USERNAME_INPUT, data["signup_username"])
        self.send_keys(RegistrationLocators.EMAIL_INPUT, data["signup_email_address"])
        self.click(RegistrationLocators.SIGN_UP_BUTTON)

    def new_registration(self, data):
        """
        A new username and EMAIL_INPUT for new user login. Get the data from Excel file having the following attribute
            signup_username: get username from faker module.
            signup_email_address: get EMAIL_INPUT from faker module.
            password: get password from excel
            day: integer from 1 to 31
            month: month from January to December.
            year: get integer from excel file.
            First_name:first USERNAME_INPUT of user.
            last_name: last USERNAME_INPUT of user.
            company: company USERNAME_INPUT of user.
            address_1: address of user having string max length 50.
            address_2: address of user having string max length 50.
            address_3: address of user having string max length 50.
            country_name: country USERNAME_INPUT of user.
            state_name: state USERNAME_INPUT of user.
            city_name: city USERNAME_INPUT of user.
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

        self.click(RegistrationLocators.NEWS_LATTER_CHECKBOX)
        self.click(RegistrationLocators.SPECIAL_OFFER_CHECKBOX)

        self.scroll_to_element(RegistrationLocators.FIRST_NAME_INPUT)
        self.send_keys(RegistrationLocators.FIRST_NAME_INPUT, data["first_name"])
        self.send_keys(RegistrationLocators.LAST_NAME_INPUT, data["last_name"])
        self.send_keys(RegistrationLocators.COMPANY_INPUT, data["company"])
        self.send_keys(RegistrationLocators.ADDRESS_1_INPUT, data["address_1"])
        self.send_keys(RegistrationLocators.ADDRESS_2_INPUT, data["address_2"])
        self.send_keys(RegistrationLocators.ADDRESS_3_INPUT, data["address_3"])

        self.scroll_to_element(RegistrationLocators.COUNTRY_DROPDOWN)
        self.select_by_text(RegistrationLocators.COUNTRY_DROPDOWN, data["country_name"])
        self.send_keys(RegistrationLocators.STATE_INPUT, data["state_name"])
        self.send_keys(RegistrationLocators.CITY_INPUT, data["city_name"])
        self.send_keys(RegistrationLocators.ZIPCODE_INPUT, data["zip_code"])
        self.scroll_to_element(RegistrationLocators.MOBILE_NUMBER_INPUT)
        self.send_keys(RegistrationLocators.MOBILE_NUMBER_INPUT, data["mobile_number"])
        self.click(RegistrationLocators.CREATE_ACCOUNT_BUTTON)
        self.wait_visible(RegistrationLocators.SUCCESSFUL_CREATE_MESSAGE_TEXT)
