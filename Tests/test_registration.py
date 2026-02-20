import pytest
from Pages.registration_page import RegistrationPage
from Utilities.excel_reader import get_registration_data


class TestRegistration:
    """Test suite for verifying user registration functionality."""
    @pytest.mark.parametrize("data", get_registration_data())
    def test_registration(self, driver, logger, data):
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

        rp.new_registration(data)
