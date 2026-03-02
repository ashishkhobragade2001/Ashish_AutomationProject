"""
Module to generate test user data using Faker.
"""

from faker import Faker


class UserFactory:
    """
    Factory class to generate fake user registration data.
    """

    fake = Faker("en_IN")

    @classmethod
    def generate_user(cls) -> dict:
        """
        Generate complete fake registration user data.

        :return: Dictionary containing user registration details.
        """
        return {
            "signup_username": cls.fake.user_name(),
            "signup_email_address": cls.fake.email(domain="gmail.com"),
            "password": cls.fake.password(),
            "first_name": cls.fake.first_name_male(),
            "last_name": cls.fake.last_name(),
            "mobile_number": cls.fake.numerify(text="9#########"),
            "company": cls.fake.company(),
            "address_1": cls.fake.street_address(),
            "address_2": cls.fake.street_name(),
            "country_name": "India",
            "state_name": cls.fake.state(),
            "city_name": cls.fake.city(),
            "zip_code": cls.fake.zipcode_in_state(state_abbr="MH"),
        }
