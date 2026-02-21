import time
from faker import Faker

from Locators.registration_locators import RegistrationLocators
from Utilities.base_page import BasePage


class RegistrationPage(BasePage):

    def is_username_email_unique(self):
        return self.is_element_visible(RegistrationLocators.enter_account_creation_message)

    def is_registration_successful(self):
        return self.is_element_visible(RegistrationLocators.successfully_create_message)

    def new_user_signup(self, data):
        # ------ for fake username an email address
        fake = Faker()
        data["signup_username"] = fake.user_name()
        data["signup_email_address"] = fake.email(domain="outlook")
        self.log_info(f"username: {data["signup_username"]}")
        self.log_info(f"signup_email_address: {data["signup_email_address"]}")

        # ------ for new sign in username and password
        self.click(RegistrationLocators.signin_tap)
        self.send_keys(RegistrationLocators.name, data["signup_username"])
        self.send_keys(RegistrationLocators.email, data["signup_email_address"])
        self.click(RegistrationLocators.signup_button)

    def new_registration(self, data):
        """
        A new username and email for new user login. Get the data from Excel file having the following attribute
            signup_username: get username from faker module.
            signup_email_address: get email from faker module.
            password: get password from excel
            day: integer from 1 to 31
            month: month from January to December.
            year: get integer from excel file.
            First_name:first name of user.
            last_name: last name of user.
            company: company name of user.
            address_1: address of user having string max length 50.
            address_2: address of user having string max length 50.
            address_3: address of user having string max length 50.
            country_name: country name of user.
            state_name: state name of user.
            city_name: city name of user.
            zip_code: zip code in integer having max length 6 digit.
            Mobile_number: 10 digit integer.

        :param data: Read value from Excel.
        :return: True if expected equal to actual else False.
        """
        # ----- new registration details
        self.click(RegistrationLocators.mr_title)
        self.send_keys(RegistrationLocators.password, data["password"])
        self.scroll_to_element(RegistrationLocators.dropdown_days)
        self.select_by_value(RegistrationLocators.dropdown_days, data["day"])
        self.select_by_text(RegistrationLocators.dropdown_months, data["month"])
        self.select_by_value(RegistrationLocators.dropdown_years, data["year"])

        self.click(RegistrationLocators.newsletter)
        self.click(RegistrationLocators.special_offer)

        self.scroll_to_element(RegistrationLocators.first_name)
        self.send_keys(RegistrationLocators.first_name, data["first_name"])
        self.send_keys(RegistrationLocators.last_name, data["last_name"])
        self.send_keys(RegistrationLocators.company, data["company"])
        self.send_keys(RegistrationLocators.address_1, data["address_1"])
        self.send_keys(RegistrationLocators.address_2, data["address_2"])
        self.send_keys(RegistrationLocators.address_3, data["address_3"])

        self.scroll_to_element(RegistrationLocators.dropdown_country)
        self.select_by_text(RegistrationLocators.dropdown_country, data["country_name"])
        self.send_keys(RegistrationLocators.state, data["state_name"])
        self.send_keys(RegistrationLocators.city, data["city_name"])
        self.send_keys(RegistrationLocators.zipcode, data["zip_code"])
        self.scroll_to_element(RegistrationLocators.mobile_number)
        self.send_keys(RegistrationLocators.mobile_number, data["mobile_number"])
        self.click(RegistrationLocators.create_account_button)
        self.wait_visible(RegistrationLocators.successfully_create_message)

