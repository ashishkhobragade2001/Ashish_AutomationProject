import pytest
from Pages.login_page import LoginPage
from Utilities.excel_reader import get_login_data

"""@pytest.mark.parametrize("EMAIL_INPUT,password", [
    ("test1@mail.com", "12345"),
    ("test2@mail.com", "wrongpass")
])
def test_login(driver, EMAIL_INPUT, password):
    lp = LoginPage(driver)
    lp.open_login()
    lp.login(EMAIL_INPUT, password)"""


@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_result", get_login_data())
def test_login(driver, logger, username, password, expected_result):
    lp = LoginPage(driver, logger)
    lp.login(username, password)

    actual_result = "success" if lp.is_login_successful() else "failure"
    assert actual_result == expected_result, f"Expected: {expected_result} but we got: {actual_result}"
