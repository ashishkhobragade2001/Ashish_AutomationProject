import pymysql
import os
from dotenv import load_dotenv


load_dotenv()


class RegistrationDatabase:

    def __init__(self, logger):
        self.logger = logger
        self.connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.connection.cursor()
        self.logger.info("Database connection successful")

    def insert_user(self, data):
        query = """
        INSERT INTO users 
        (username, email, password, first_name, last_name, company, address_1,
         address_2, country, state, city, zip_code, mobile_number)
        VALUES (%s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            data["signup_username"],
            data["signup_email_address"],
            data["password"],
            data["first_name"],
            data["last_name"],
            data["company"],
            data["address_1"],
            data["address_2"],
            data["country_name"],
            data["state_name"],
            data["city_name"],
            data["zip_code"],
            data["mobile_number"],
        )

        self.cursor.execute(query, values)
        self.connection.commit()
        self.logger.info("User inserted successfully")

    def user_exists(self, email):
        query = "SELECT * FROM users WHERE email=%s"
        self.cursor.execute(query, (email,))
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
