import time

import pytest

from Locators.products_locators import ProductLocators
from Utilities.base_page import BasePage


class ProductPage(BasePage):

    @pytest.mark.description("Go to Home page and Sign in")
    def login_to_webpage(self, username, password):
        self.click(ProductLocators.sign_in_tap)
        self.send_keys(ProductLocators.username, username)
        self.send_keys(ProductLocators.password, password)
        self.click(ProductLocators.login_button)
        self.log_info("click on login button an wait for 2 second")
        self.wait_visible(ProductLocators.logout_button)
        # time.sleep(5)
        self.close_google_vignette_ad()

    def login_verification(self):
        expected_title = self.get_title()
        self.log_info(f"expected title is:{expected_title}")
        actual_title = "Automation Exercise"
        assert actual_title == expected_title, f"Login Fail Expected title:{expected_title} but got :{actual_title}"

    @pytest.mark.description("Go to product tab and select the product")
    def select_products(self):
        self.log_info("product selection method start")
        self.close_google_vignette_ad()
        self.wait_visible(ProductLocators.product_tap)
        self.click(ProductLocators.product_tap)
        time.sleep(2)
        self.close_google_vignette_ad()
        self.log_info("before move to kis tab")
        self.scroll_to_element(ProductLocators.kids_tap)
        self.log_info("yes move to kis tab")
        self.click(ProductLocators.kids_tap)
        self.log_info("click on kids tab")
        self.click(ProductLocators.dress_tap)
        self.scroll_to_element(ProductLocators.view_product)
        self.click(ProductLocators.view_product)
        self.click(ProductLocators.add_to_cart)
        self.click(ProductLocators.continue_shopping_button)
        self.log_info("before click on cart tap")
        self.click(ProductLocators.cart_tap)
        self.log_info("yes click on cart tap")
        self.click(ProductLocators.proceed_to_checkout_button)
        self.scroll_to_element(ProductLocators.place_order_button)
        self.click(ProductLocators.place_order_button)
        self.log_info("click on sign in tab and wait for 5 sec")
        time.sleep(3)

    #@pytest.mark.description("Verify user can add product to cart")
    def card_details_page(self, name_on_card, card_number, cvv_number, expiry_month, expiry_year):
        self.close_google_vignette_ad()
        self.log_info("card verification method start ")
        self.wait_visible(ProductLocators.name_on_card)
        self.log_info("wait  until payment page not visible")
        self.send_keys(ProductLocators.name_on_card, name_on_card)
        self.log_info("entered name of card")
        self.send_keys(ProductLocators.card_number, card_number)
        self.scroll_to_element(ProductLocators.cvv)
        self.send_keys(ProductLocators.cvv, cvv_number)
        self.send_keys(ProductLocators.expiry_month, expiry_month)
        self.send_keys(ProductLocators.expiry_year, expiry_year)
        self.scroll_to_element(ProductLocators.submit_button)
        self.click(ProductLocators.submit_button)
        self.log_info("click on submit button")
        time.sleep(3)

    def order_verification(self):
        self.close_google_vignette_ad()
        self.log_info("order verification process start ")
        success_message = self.get_text(ProductLocators.order_place_verification_text)
        self.log_info(f"success message: {success_message}")
        assert success_message == "ORDER PLACED!"
        self.click(ProductLocators.download_invoice)
        self.log_info("download invoice")
