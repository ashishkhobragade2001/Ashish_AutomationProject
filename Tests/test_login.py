import pytest
from Pages.login_page import LoginPage

@pytest.mark.parametrize("email,password", [
    ("test1@mail.com", "12345"),
    ("test2@mail.com", "wrongpass")
])
def test_login(driver, email, password):
    lp = LoginPage(driver)
    lp.open_login()
    lp.login(email, password)
