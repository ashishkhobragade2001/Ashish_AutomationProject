from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os, time


class BasePage:

    def __init__(self, driver):
        self.logger = None
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def select_dropdown(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)

    def select_by_text(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        Select(self.driver.find_element(*locator)).select_by_value(value)

    def select_by_index(self, locator, index):
        Select(self.driver.find_element(*locator)).select_by_index(index)

    def wait_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def take_screenshot(self, name):
        path = f"Screenshots/{name}_{int(time.time())}.png"
        self.driver.save_screenshot(path)

    def switch_to_new_window(self):
        parent = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break
    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def safe_action(self, action_name, locator, action, value=None):
        try:
            #self.logger.info(f"Performing action: {action_name}")
            element = self.driver.find_element(*locator)

            if action == "click":
                element.click()
            elif action == "send_keys":
                element.send_keys(value)

        except Exception as e:
            #self.logger.error(f"Error in {action_name}: {e}")
            self.take_screenshot(action_name)
            raise

    def wait_for_alert(self, timeout=5):
        self.logger.info("Waiting for alert to be present")
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            self.logger.error("Alert did not appear")
            return False

