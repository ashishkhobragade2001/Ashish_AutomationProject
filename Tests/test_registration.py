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
            2. Enter account credentials (username, EMAIL_INPUT, password).
            3. Validate username and EMAIL_INPUT is unique.
            4. Enter personal details.
            5. Submit the registration form.
            6. Validate registration is successful or not.

        Expected Result:
            The user registration should complete successfully without errors,
            and the account should be created.
        """
        rp = RegistrationPage(driver, logger)

        # ---- New user Sign up
        rp.new_user_signup(data)
        actual_result = "pass" if rp.is_username_email_unique() else "fail"
        assert actual_result == "pass", "username or EMAIL_INPUT address not unique."

        # ---- New Registration page (Personal information form)
        rp.new_registration(data)
        registration_result = "success" if rp.is_registration_successful() else "failure"
        assert registration_result == data["expected_result"], \
            f"Expected: {data["expected_result"]} but we got: {registration_result}"
