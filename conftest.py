import pytest
import os
import allure
from datetime import datetime
from selenium import webdriver
from pytest_html import extras
from Utilities.logger import Logger


# 🌟 CREATE DYNAMIC REPORT FOLDER
def pytest_configure(config):
    # timestamp folder
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    base_report_dir = os.path.join("Reports", f"report_{timestamp}")
    config.base_report_dir = base_report_dir
    allure_dir = os.path.join(base_report_dir, "allure_reports")
    screenshot_dir = os.path.join(base_report_dir, "screenshots")

    # 🔥 HTML report path set karna
    config.option.htmlpath = os.path.join(base_report_dir, "report.html")

    os.makedirs(allure_dir, exist_ok=True)
    os.makedirs(screenshot_dir, exist_ok=True)

    # Store paths globally
    config.option.allure_report_dir = allure_dir
    config._metadata = getattr(config, "_metadata", {})
    config._metadata["Report Folder"] = base_report_dir


# 🌟 DRIVER FIXTURE
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")
    yield driver
    driver.quit()


# 🌟 LOGGER FIX
@pytest.fixture(scope="session")
def logger(request):
    log = Logger(request.config.base_report_dir).get_logger()
    return log


# 📸 SCREENSHOT + ATTACH IN HTML
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            file_name = f"{item.name}.png"
            base_dir = item.config.base_report_dir
            screenshot_path = os.path.join(base_dir, "screenshots", file_name)
            driver.save_screenshot(screenshot_path)

            # 📌 Attach to HTML Report
            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot_path))
            report.extra = extra

            # 📌 Attach to Allure Report
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


# 🌟 METADATA
def pytest_metadata(metadata):
    metadata["Project"] = "Automation Exercise"
    metadata["Tester"] = "Ashish"
    metadata["Browser"] = "Chrome"
    metadata["Framework"] = "Pytest + Selenium"


# 🌟 DESCRIPTION COLUMN
def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{getattr(report, "description", "")}</td>')
