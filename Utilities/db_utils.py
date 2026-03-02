import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


class RegistrationDatabase:
    """
    RegistrationDatabase handles all database operations
    related to user registration.

    This class provides methods to:
    - Establish database connection
    - Insert a new user record
    - Verify if a user exists
    - Close database connection safely
    """

    def __init__(self, logger):
        """
        Initialize database connection using environment variables.

        Args:
            logger: Logger instance for logging DB operations.
        """
        self.logger = logger
        self.connection = None
        self.cursor = None

        try:
            self.connection = pymysql.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            self.cursor = self.connection.cursor()
            self.logger.info("Database connection established successfully.")

        except Exception as e:
            self.logger.error(f"Database connection failed: {e}")
            raise

    def insert_user(self, data):
        """
        Insert a new user record into the users table.

        Args:
            data (dict): Dictionary containing user registration details.

        Raises:
            Exception: If insertion fails.
        """
        query = """
        INSERT INTO users 
        (username, email, password, first_name, last_name, company, address_1,
         address_2, country, state, city, zip_code, mobile_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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

        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            self.logger.info(
                f"User inserted successfully into DB. Email: {data['signup_email_address']}"
            )

        except Exception as e:
            self.connection.rollback()
            self.logger.error(f"Failed to insert user: {e}")
            raise

    def user_exists(self, email):
        """
        Check whether a user exists in the database.

        Args:
            email (str): Email address to check.

        Returns:
            list: List of matching records (empty if none found).
        """
        query = "SELECT * FROM users WHERE email=%s"

        try:
            self.cursor.execute(query, (email,))
            result = self.cursor.fetchall()

            self.logger.info(
                f"User existence check completed. Records found: {len(result)} for email: {email}"
            )

            return result

        except Exception as e:
            self.logger.error(f"Error while checking user existence: {e}")
            raise

    def close(self):
        """
        Close database cursor and connection safely.
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

            self.logger.info("Database connection closed successfully.")

        except Exception as e:
            self.logger.error(f"Error while closing database connection: {e}")
