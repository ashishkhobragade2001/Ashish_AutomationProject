"""
Test Module: Product Purchase Flow

Description:
This module contains end-to-end test cases for validating the product
purchase workflow on the Automation Exercise website.

Framework: Pytest
Design Pattern: Page Object Model (POM)
Author: Ashish Khobragade
"""

import pytest
from Pages.products_page import ProductPage


class TestProducts:
    """
    Test suite for validating product selection and order placement.
    """

    @pytest.mark.smoke
    @pytest.mark.products_add_to_cart
    def test_products_add_to_carts(self, driver, logger):
        """
        Test Case: Verify user can Log in, select products, enter card details,
        and successfully place an order.

        Steps:
        1. Launch website
        2. Login with valid credentials
        3. Verify successful login
        4. Select products and proceed to checkout
        5. Enter card details
        6. Verify order confirmation

        Expected Result:
        User should be able to complete the purchase flow without errors.
        """

        logger.info("\nStarting test: Product Add To Cart")

        product_page = ProductPage(driver, logger)
        product_page.login_to_webpage(
            username="ashish@outlook.com",
            password="ashish123"
        )
        product_page.login_verification()
        product_page.select_products()
        product_page.card_details_page(
            name_on_card="Neha Seth",
            card_number=111144443333,
            cvv_number=123,
            expiry_month=12,
            expiry_year=2032
        )

        logger.info("Verifying order confirmation")
        product_page.order_verification()

        logger.info("Test completed successfully")
