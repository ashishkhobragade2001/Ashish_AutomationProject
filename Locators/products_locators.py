from selenium.webdriver.common.by import By


class ProductLocators:
    """
    Locators for Product Purchase Flow.

    This class contains all web element locators related to:
    - User Login
    - Product Selection
    - Cart & Checkout
    - Payment Details
    - Order Confirmation

    These locators are used by the ProductPage class to perform
    user actions during automation of the product purchase workflow.
    """

    # 🔐 Authentication
    SIGN_IN_TAB = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
    USER_NAME_INPUT = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[2]")
    PASSWORD_INPUT = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[3]")
    LOGIN_BUTTON = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")
    LOGOUT_BUTTON = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")

    # 🛍 Product Navigation
    PRODUCT_TAB = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]")
    KIDS_TAB = (By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/h4[1]/a[1]")
    DRESS_TAB = (By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/ul[1]/li[1]/a[1]")
    VIEW_PRODUCT_TAB = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/a[1]")

    # 🛒 Cart Actions
    ADD_TO_CART_TAB = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/button[1]")
    CONTINUE_SHOPING_BUTTON = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]")
    CART_TAB = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]")
    PLACE_ORDER_BUTTON = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[7]/a[1]")

    # 💳 Payment Details
    NAME_ON_CARD_INPUT = (By.XPATH, "//input[@USERNAME_INPUT='name_on_card']")
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@USERNAME_INPUT='card_number']")
    CVV_INPUT = (By.XPATH, "//input[@USERNAME_INPUT='cvc']")
    EXPIRY_MONTH_INPUT = (By.XPATH, "//input[@USERNAME_INPUT='expiry_month']")
    EXPIRY_YEAR_INPUT = (By.XPATH, "//input[@USERNAME_INPUT='expiry_year']")
    SUBMIT_BUTTON_INPUT = (By.XPATH, "//button[@id='submit']")

    # ✅ Order Confirmation
    ORDER_TEXT_VERIFICATION_TEXT = (By.XPATH, "//b[text()='Order Placed!']")
    DOWNLOAD_INVOICE_BUTTON = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/a[1]")
