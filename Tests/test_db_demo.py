import pytest
from Utilities.db_utils import RegistrationDatabase


@pytest.mark.database
def test_demo_db_insert(logger):

    demo_data = {
        "signup_username": "demo_user_automation_1",
        "signup_email_address": "demo_user1@test.com",
        "first_name": "Demo",
        "last_name": "User",
        "company": "TestCompany",
        "address_1": "Street 1",
        "address_2": "Street 2",
        "country_name": "India",
        "state_name": "Gujarat",
        "city_name": "Ahmedabad",
        "zip_code": "380001",
        "mobile_number": "9999999999"
    }

    db = RegistrationDatabase(logger)

    try:
        logger.info("Inserting demo user into DB...")
        db.insert_user(demo_data)

        logger.info("Checking if demo user exists in DB...")
        result = db.user_exists(demo_data["signup_email_address"])

        assert len(result) == 1, "Demo user not inserted in DB"

        logger.info("Demo DB test passed successfully")
    finally:
        pass

