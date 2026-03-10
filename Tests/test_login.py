import pytest
from Pages.login_page import LoginPage
from Utilities.excel_reader import get_login_data


@pytest.mark.login
@pytest.mark.parametrize("username, password, expected_result", get_login_data())
def test_login(driver, logger, username, password, expected_result):
    lp = LoginPage(driver, logger)
    lp.login(username, password)

    actual_result = "success" if lp.is_login_successful() else "failure"
    assert actual_result == expected_result, f"Expected: {expected_result} but we got: {actual_result}"


# file update
# test for pole scm