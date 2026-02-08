import pytest
import os
import datetime
from selenium import webdriver
from Utilities.logger import Logger

def pytest_configure(config):
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    report_path = os.path.join("Reports", f"report_{timestamp}")
    os.makedirs(report_path, exist_ok=True)

    # Save path globally
    config.option.htmlpath = os.path.join(report_path, "report.html")
    config.option.allure_report_dir = os.path.join(report_path, "allure-results")
    config._report_path = report_path


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # 🔥 PASSWORD POPUPS OFF
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }

    options.add_experimental_option("prefs", prefs)

    # 🔥 NOTIFICATIONS OFF
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")


    # 🔥 INFO BARS OFF
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")
    yield driver
    driver.quit()


# 📸 Screenshot on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = os.path.join(item.config._report_path, "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            driver.save_screenshot(os.path.join(screenshot_dir, f"{item.name}.png"))

@pytest.fixture(scope="session")
def report_path():
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    path = os.path.join("Reports", f"report_{timestamp}")
    os.makedirs(path, exist_ok=True)
    return path

@pytest.fixture(scope="session")
def logger(report_path):
    log = Logger(report_path).get_logger()
    return log