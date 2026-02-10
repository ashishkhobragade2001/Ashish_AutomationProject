from selenium.webdriver.common.by import By


class ProductLocators:
    sign_in_tap = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
    username = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[2]")
    password = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[3]")
    login_button = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")

    logout_button = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
    product_tap = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]")
    kids_tap = (By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/h4[1]/a[1]")
    dress_tap = (By.XPATH, "/html[1]/body[1]/section[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/ul[1]/li[1]/a[1]")

    view_product = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/a[1]")
    add_to_cart = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/span[1]/button[1]")
    continue_shopping_button = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[1]")
    cart_tap = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]")
    proceed_to_checkout_button = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]")
    place_order_button = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[7]/a[1]")

    name_on_card = (By.XPATH, "//input[@name='name_on_card']")
    card_number = (By.XPATH, "//input[@name='card_number']")
    cvv = (By.XPATH, "//input[@name='cvc']")
    expiry_month = (By.XPATH, "//input[@name='expiry_month']")
    expiry_year = (By.XPATH, "//input[@name='expiry_year']")
    submit_button = (By.XPATH, "//button[@id='submit']")

    order_place_verification_text = (By.XPATH, "//b[text()='Order Placed!']")
    download_invoice = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/a[1]")





