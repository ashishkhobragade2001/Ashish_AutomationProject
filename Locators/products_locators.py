from selenium.webdriver.common.by import By


class ProductLocators:
    sign_in_tap = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]")
    username = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[2]")
    password = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/input[3]")
    login_button = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]")

    product_tap = (By.XPATH, "/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]")
    kids_tap = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/h4[1]/a[1]")
    dress_tap = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/ul[1]/li[1]/a[1]")
    


