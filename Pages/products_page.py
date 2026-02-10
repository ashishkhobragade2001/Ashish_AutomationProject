"""
Page Module: Product Page

Description:
Contains all actions related to product browsing, cart handling,
payment, and order verification for Automation Exercise website.

Design Pattern: Page Object Model (POM)
Author: Ashish Khobragade
"""

from Locators.products_locators import ProductLocators
from Utilities.base_page import BasePage


class ProductPage(BasePage):
    """
    Page Object representing product purchase workflow.
    """

    def login_to_webpage(self, username: str, password: str) -> None:
        """
        Logs into the application using valid credentials.

        :argument
            username(str): User email
            password(str): User password
        :returns
            bool: True if log in successfully
        """
        self.log_info("Navigating to login page")
        self.click(ProductLocators.sign_in_tap)

        self.log_info("Entering login credentials")
        self.send_keys(ProductLocators.username, username)
        self.send_keys(ProductLocators.password, password)

        self.log_info("Clicking login button")
        self.click(ProductLocators.login_button)

        self.wait_visible(ProductLocators.logout_button)
        self.close_google_vignette_ad()
        self.log_info("Login successful")

    def login_verification(self) -> None:
        """
        Verifies successful login by checking page title.
        """
        expected_title = "Automation Exercise"
        actual_title = self.get_title()

        self.log_info(f"Verifying page title: {actual_title}")
        assert actual_title == expected_title, \
            f"Login failed. Expected title '{expected_title}', but got '{actual_title}'"

    def select_products(self) -> None:
        """
        Selects product from Kids → Dress category and proceeds to checkout.
        """
        self.log_info("Starting product selection flow")
        self.close_google_vignette_ad()

        self.wait_visible(ProductLocators.product_tap)
        self.click(ProductLocators.product_tap)
        self.close_google_vignette_ad()
        self.scroll_to_element(ProductLocators.kids_tap)
        self.click(ProductLocators.kids_tap)
        self.log_info("Navigated to Kids category")

        self.click(ProductLocators.dress_tap)
        self.log_info("Selected Dress category")

        self.scroll_to_element(ProductLocators.view_product)
        self.click(ProductLocators.view_product)

        self.click(ProductLocators.add_to_cart)
        self.click(ProductLocators.continue_shopping_button)
        self.log_info("Product added to cart")

        self.click(ProductLocators.cart_tap)
        self.click(ProductLocators.proceed_to_checkout_button)

        self.scroll_to_element(ProductLocators.place_order_button)
        self.click(ProductLocators.place_order_button)
        self.log_info("Proceeded to checkout")

    def card_details_page(self, name_on_card: str, card_number: str,
                          cvv_number: str, expiry_month: str,
                          expiry_year: str) -> None:
        """
        Enters payment card details and submits order.

         :arg
             name_on_card(str): cardholder name
             card_number(str): card number
             cvv_number(int): CVV number
             expiry_month(int): Expiry Month
             expiry_year(int): Expiry Year
        :returns
            bool: True if payment successfully

        """
        self.close_google_vignette_ad()
        self.log_info("Entering card details")

        self.wait_visible(ProductLocators.name_on_card)
        self.send_keys(ProductLocators.name_on_card, name_on_card)
        self.send_keys(ProductLocators.card_number, card_number)

        self.scroll_to_element(ProductLocators.cvv)
        self.send_keys(ProductLocators.cvv, cvv_number)
        self.send_keys(ProductLocators.expiry_month, expiry_month)
        self.send_keys(ProductLocators.expiry_year, expiry_year)

        self.scroll_to_element(ProductLocators.submit_button)
        self.click(ProductLocators.submit_button)

        self.log_info("Payment submitted successfully")

    def order_verification(self) -> None:
        """
        Verifies order success message and downloads invoice.
        """
        self.close_google_vignette_ad()
        self.log_info("Verifying order placement")

        success_message = self.get_text(ProductLocators.order_place_verification_text)
        self.log_info(f"Order message displayed: {success_message}")

        assert success_message == "ORDER PLACED!", \
            f"Order verification failed. Expected 'ORDER PLACED!' but got '{success_message}'"

        self.click(ProductLocators.download_invoice)
        self.log_info("Invoice downloaded")
