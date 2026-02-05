import pytest
from Pages.registration_page import RegistrationPage


class TestRegistration:

    def test_registration(self, driver, logger):
        rp = RegistrationPage(driver, logger)

        rp.new_registration(
            username="ashish",
            email_address="sa745am@outlook.com",
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