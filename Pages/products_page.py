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
            username(str): User username
            password(str): User password
        :returns
            bool: True if log in successfully
        """
        self.click(ProductLocators.SIGN_IN_TAB, "sign in tab")
        self.send_keys(ProductLocators.USER_NAME_INPUT, username, "user name ")
        self.send_keys(ProductLocators.PASSWORD_INPUT, password, "password")
        self.click(ProductLocators.LOGIN_BUTTON,"Login button")

        self.wait_visible(ProductLocators.LOGOUT_BUTTON, "log out Button")
        self.close_google_vignette_ad()

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
        self.close_google_vignette_ad()
        self.wait_visible(ProductLocators.PRODUCT_TAB, "product tab")
        self.click(ProductLocators.PRODUCT_TAB, "product tab")
        self.close_google_vignette_ad()
        self.scroll_to_element(ProductLocators.KIDS_TAB, "kids tab")
        self.click(ProductLocators.KIDS_TAB, "kids tab")
        self.click(ProductLocators.DRESS_TAB,"dress tab")
        self.scroll_to_element(ProductLocators.VIEW_PRODUCT_TAB, "view product tab")
        self.click(ProductLocators.VIEW_PRODUCT_TAB, "view product tab")
        self.click(ProductLocators.ADD_TO_CART_TAB, "add to cart tab")
        self.click(ProductLocators.CONTINUE_SHOPING_BUTTON,"continue on shopping button")

        self.click(ProductLocators.CART_TAB, "cart tab")
        self.click(ProductLocators.PROCEED_TO_CHECKOUT_BUTTON, "proceed to checkout button")
        self.scroll_to_element(ProductLocators.PLACE_ORDER_BUTTON, "place order button")
        self.click(ProductLocators.PLACE_ORDER_BUTTON, "place order button")

    def card_details_page(self, name_on_card: str, card_number: int,
                          cvv_number: int, expiry_month: int,
                          expiry_year: int) -> None:
        """
        Enters payment card details and submits order.

         :argument
             name_on_card(str): cardholder USERNAME_INPUT
             card_number(str): card number
             cvv_number(int): CVV number
             expiry_month(int): Expiry Month
             expiry_year(int): Expiry Year
        :returns
            bool: True if payment successfully
        """
        self.close_google_vignette_ad()
        self.wait_visible(ProductLocators.NAME_ON_CARD_INPUT, "name on card")
        self.send_keys(ProductLocators.NAME_ON_CARD_INPUT, name_on_card, "name on card")
        self.send_keys(ProductLocators.CARD_NUMBER_INPUT, card_number, "card number")

        self.scroll_to_element(ProductLocators.CVV_INPUT, "cvv ")
        self.send_keys(ProductLocators.CVV_INPUT, cvv_number, "cvv")
        self.send_keys(ProductLocators.EXPIRY_MONTH_INPUT, expiry_month, "expiry month")
        self.send_keys(ProductLocators.EXPIRY_YEAR_INPUT, expiry_year, "expiry year")
        self.scroll_to_element(ProductLocators.SUBMIT_BUTTON_INPUT, "submit button")
        self.click(ProductLocators.SUBMIT_BUTTON_INPUT, "submit button")

    def order_verification(self) -> None:
        """
        Verifies order success message and downloads invoice.
        """
        self.close_google_vignette_ad()
        self.log_info("Verifying order placement")
        success_message = self.get_text(ProductLocators.ORDER_TEXT_VERIFICATION_TEXT)
        self.log_info(f"Order message displayed: {success_message}")

        assert success_message == "ORDER PLACED!", \
            f"Order verification failed. Expected 'ORDER PLACED!' but got '{success_message}'"

        self.click(ProductLocators.DOWNLOAD_INVOICE_BUTTON,"download invoice")
        self.log_info("Invoice downloaded")
