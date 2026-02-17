import pytest
from Pages.registration_page import RegistrationPage


class TestRegistration:
    """Test suite for verifying user registration functionality."""

    def test_registration(self, driver, logger):
        """
        Verify that a new user can successfully complete the registration process.

        This test uses the RegistrationPage page object to fill in all required
        user details and submit the registration form.

        Args:
            driver (WebDriver): Selenium WebDriver instance provided by pytest fixture.
            logger (Logger): Logger instance used to record test execution steps.

        Steps:
            1. Open the registration page.
            2. Enter account credentials (username, email, password).
            3. Select date of birth.
            4. Enter personal and address details.
            5. Submit the registration form.

        Expected Result:
            The user registration should complete successfully without errors,
            and the account should be created.
        """
        rp = RegistrationPage(driver, logger)

        rp.new_registration(
            username="ashish",
            email_address="sa635am@outlook.com",
            password="saran@002",
            day="6",
            month="April",
            year="1994",
            first_name="sanar",
            last_name="dube",
            company="Mumbai",
            address_1="panchashl bagar",
            address_2="sane gurugi",
            address_3="bhag 2",
            country_name="India",
            state_name="Maharashtra",
            city_name="Yavatmal",
            zip_code="445563",
            mobile_number="9988774455"
        )
