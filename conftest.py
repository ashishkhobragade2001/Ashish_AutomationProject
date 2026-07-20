import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import base64
import allure
from datetime import datetime
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

    # useful for Jenkins.
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.get("https://automationexercise.com/")

    yield driver
    driver.quit()


# 🌟 LOGGER FIX
@pytest.fixture(scope="session")
def logger(request):
    log = Logger(request.config.base_report_dir).get_logger()
    return log


# 📸 SCREENSHOT + ATTACH IN ALLURE

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

            # Save screenshot file (for folder record)
            driver.save_screenshot(screenshot_path)

            # ✅ Convert image to base64 (THIS FIXES HTML)
            with open(screenshot_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()

            extra = getattr(report, "extra", [])
            extra.append(extras.image(encoded_string, mime_type="image/png"))
            report.extra = extra

            # ✅ Allure attach
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


# 🌟 METADATA
def pytest_metadata(metadata):
    metadata["Project"] = "Automation Exercise"
    metadata["Tester"] = "Ashish Khobragade"
    metadata["Browser"] = "Chrome"
    metadata["Framework"] = "Pytest + Selenium"


# 🌟 DESCRIPTION COLUMN
def pytest_html_results_table_header(cells):
    cells.insert(2, '<th>Description</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{getattr(report, "description", "")}</td>')

