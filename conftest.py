import pytest
import os
import datetime
from selenium import webdriver

def pytest_configure(config):
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    report_path = os.path.join("Reports", f"report_{timestamp}")
    os.makedirs(report_path, exist_ok=True)

    # Save path globally
    config.option.htmlpath = os.path.join(report_path, "report.html")
    config.option.allure_report_dir = os.path.join(report_path, "allure-results")
    config._report_path = report_path


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
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
