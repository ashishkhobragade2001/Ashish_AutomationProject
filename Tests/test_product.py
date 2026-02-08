from Locators.products_locators import ProductLocators
from Pages.products_page import ProductPage
from Utilities.base_page import BasePage


class TestProducts:

    def test_products_add_to_carts(self, driver, logger):
        pp = ProductPage(driver, logger)
        pp.login_to_webpage(username="ashish@outlook.com", password="ashish123")
        pp.select_products()
        pp.card_details_page(
            name_on_card="Sagar Seth",
            card_number="111144443333",
            cvv_number="123",
            expiry_month="12",
            expiry_year="2032")
        pp.order_verification()
