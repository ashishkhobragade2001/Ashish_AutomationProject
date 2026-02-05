import time
from Locators.registration_locators import RegistrationLocators
from Utilities.base_page import BasePage


class RegistrationPage(BasePage):

    def new_registration(self, username, email_address, password, day,
                         month, year, first_name, last_name, company,
                         address_1, address_2, address_3, country_name,
                         state_name, city_name, zip_code, mobile_number):
        self.click(RegistrationLocators.signin_tap)

        self.send_keys(RegistrationLocators.name, username)
        self.send_keys(RegistrationLocators.email, email_address)
        self.click(RegistrationLocators.signup_button)

        self.log_info("validate text 'Enter Account Information' has been kipped")
        #validate_text = self.get_text(RegistrationLocators.validation_text)
        #assert  validate_text == "Enter Account Information"
        self.log_info("click on on mr_Title")
        self.click(RegistrationLocators.mr_title)

        self.send_keys(RegistrationLocators.password, password)
        self.select_dropdown(RegistrationLocators.dropdown_days, day)
        self.select_dropdown(RegistrationLocators.dropdown_months, month)
        self.select_dropdown(RegistrationLocators.dropdown_years, year)

        self.click(RegistrationLocators.newsletter)
        self.click(RegistrationLocators.special_offer)

        self.send_keys(RegistrationLocators.first_name, first_name)
        self.send_keys(RegistrationLocators.last_name, last_name)
        self.send_keys(RegistrationLocators.company, company)
        self.send_keys(RegistrationLocators.address_1, address_1)
        self.send_keys(RegistrationLocators.address_2, address_2)
        self.send_keys(RegistrationLocators.address_3, address_3)

        self.select_dropdown(RegistrationLocators.dropdown_country, country_name)
        self.send_keys(RegistrationLocators.state, state_name)
        self.send_keys(RegistrationLocators.city, city_name)
        self.send_keys(RegistrationLocators.zipcode, zip_code)
        self.send_keys(RegistrationLocators.mobile_number, mobile_number)
        self.click(RegistrationLocators.create_account_button)
        time.sleep(8)
        self.log_info("wait until Account Created! message not visible")
        # wait until Account Create message not appear
        self.wait_visible(RegistrationLocators.successfully_create_message)
        #successfully_create_message = self.get_text(RegistrationLocators.successfully_create_message)
        #assert successfully_create_message == "Account Created!"

        self.click(RegistrationLocators.continue_button)
        time.sleep(5)
        self.wait_clickable(RegistrationLocators.varification_Logout_TAP)
        self.click(RegistrationLocators.varification_Logout_TAP)
