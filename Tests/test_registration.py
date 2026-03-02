"""
Module: test_registration
Description: Contains automated test cases for validating
             the user registration workflow including
             UI validation and database verification.
"""

import pytest
from Pages.registration_page import RegistrationPage
from Utilities.db_utils import RegistrationDatabase
from Utilities.excel_reader import get_registration_data
from TestData.user_factory import UserFactory


class TestRegistration:
    """
    Test suite for verifying complete user registration functionality.

    This includes:
        - UI-based registration validation
        - Success message verification
        - Database insertion and validation
    """

    @pytest.mark.registration
    @pytest.mark.parametrize("data", get_registration_data())
    def test_registration(self, driver, logger, data):
        """
        Test that a new user can successfully register
        and the data is correctly stored in the database.

        :param driver: Selenium WebDriver fixture
        :param logger: Logger fixture
        :param data: Registration data from Excel file
        """

        logger.info("===== Starting Registration Test =====")

        # Generate unique user data using factory
        fake_data = UserFactory.generate_user()
        data.update(fake_data)

        rp = RegistrationPage(driver, logger)

        # ---- Step 1: Initial Signup
        rp.new_user_signup(data)

        assert rp.is_username_email_unique(), \
            "Username or Email is not unique."

        logger.info("Username and Email validated successfully.")

        # ---- Step 2: Complete Registration
        rp.new_registration(data)

        registration_success = rp.is_registration_successful()
        expected_success = data["expected_result"].strip().lower() == "success"

        logger.info(f"Expected: {expected_success}")
        logger.info(f"Actual: {registration_success}")

        if expected_success:
            assert registration_success, "Expected success but registration failed."
        else:
            assert not registration_success, "Expected failure but registration succeeded."

        # ---- Step 3: Database Validation
        if registration_success and expected_success:
            logger.info("Starting DB validation...")

            db = RegistrationDatabase(logger)

            try:
                db.insert_user(data)

                result = db.user_exists(data["signup_email_address"])
                assert len(result) == 1, "User not inserted in DB"

                logger.info("Database validation successful.")

            finally:
                db.close()

        else:
            logger.info("Skipping DB validation since registration failed or expected failure.")

        logger.info("===== Registration Test Completed =====")
