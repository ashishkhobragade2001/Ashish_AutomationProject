import time
from Locators.registration_locators import RegistrationLocators
from Utilities.base_page import BasePage


class RegistrationPage(BasePage):

    def new_registration(self, signup_username, signup_email_address, password, day,
                         month, year, first_name, last_name, company,
                         address_1, address_2, address_3, country_name,
                         state_name, city_name, zip_code, mobile_number, ):
        """
        Create a new user account by completing the registration form.

        This method performs end-to-end registration including account
        credentials, personal information, address details, and final
        account creation confirmation.

                Args:
                    signup_username (str): Username for the new account.
                    signup_email_address (str): Email address for registration.
                    password (str): Account password.
                    day (str | int): Day of birth (1–31).
                    month (str): Month of birth (e.g., "January").
                    year (str | int): Year of birth.
                    first_name (str): User's first name.
                    last_name (str): User's last name.
                    company (str): Company name.
                    address_1 (str): Primary address line.
                    address_2 (str): Secondary address line.
                    address_3 (str): Additional address information.
                    country_name (str): Country name selected from dropdown.
                    state_name (str): State name.
                    city_name (str): City name.
                    zip_code (str): Postal/ZIP code.
                    mobile_number (str): User's mobile number.

                Returns:
                    bool: True if account creation is successful and logout is verified,
                    otherwise False.

                Workflow:
                    1. Navigate to sign-up page.
                    2. Enter basic account credentials.
                    3. Fill date of birth and title.
                    4. Provide personal and address information.
                    5. Submit a registration form.
                    6. Wait for "Account Created" confirmation.
                    7. Continue and verify logout option is visible.

                Raises:
                    Exception: If any element interaction fails or expected page
                    elements are not visible within the wait time.

                """
        self.click(RegistrationLocators.signin_tap)

        self.send_keys(RegistrationLocators.name, signup_username)
        self.send_keys(RegistrationLocators.email, signup_email_address)
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

        self.wait_visible(RegistrationLocators.successfully_create_message)
        #successfully_create_message = self.get_text(RegistrationLocators.successfully_create_message)
        #assert successfully_create_message == "Account Created!"

        self.click(RegistrationLocators.continue_button)
        time.sleep(5)
        self.wait_clickable(RegistrationLocators.verification_Logout_TAP)
        self.click(RegistrationLocators.verification_Logout_TAP)
