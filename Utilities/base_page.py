from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


class ElementActionException(Exception):
    """custom exception for element action"""
    pass


class BasePage:
    """
        BasePage contains common reusable Selenium actions used across all Page Objects.

        This class acts as a wrapper over Selenium WebDriver and provides:
        - Element interactions (click, send keys, text fetch)
        - Wait utilities
        - Dropdown handling
        - Window handling
        - Screenshot capture
        - Safe action wrapper with error handling
        - Logging support
        - Alert handling
        - Scroll utilities
        - Ad pop-up auto close handling

        Attributes:
            driver (WebDriver): Selenium WebDriver instance.
            logger (Logger): Logger object used for logging test steps.
        """

    def __init__(self, driver, logger):
        """
        Initializes BasePage with driver and logger.
        :argument
            driver (WebDriver): Selenium WebDriver instance.
            logger (Logger): Logger instance for logging.
        """
        self.driver = driver
        self.logger = logger

        # ---------- LOGGER WRAPPER METHODS ----------

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def click(self, locator, locator_name=""):
        """
        Clicks on a web element after waiting until it becomes clickable.
        :argument
            locator (tuple): Locator strategy in format (By, value).
        """
        self.log_info(f"clicking on element: {locator_name}")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value, locator_name=""):
        """
        Clicks on a web element after waiting until it becomes clickable.
        :argument
            locator (tuple): Locator strategy in format (By, value).
        """
        self.log_info(f"Entering text: {value} in to element: {locator_name}")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        """
        Retrieves visible text from a web elements
        :argument
            locator (tuple): Locator strategy.
        :returns
            str: Text of the element.
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def get_title(self):
        """
        Retrieves title text from a web elements
        :returns
            str: Text of the element.
        """
        return self.driver.title

    def select_by_text(self, locator, text, locator_name=""):
        """
        selects an option from dropdown after waiting for visibility.
        :argument
            locator (tuple): Dropdown locator.
            text (str): Visible text to select.
        """
        self.log_info(f"selecting: {text} from dropdown: {locator_name}")
        Select(self.driver.find_element(*locator)).select_by_visible_text(str(text))

    def select_by_value(self, locator, value, locator_name=""):
        """
        selects an option from dropdown after waiting for visibility.
        :argument
            locator (tuple): Dropdown locator.
            text (str): Visible text to select.
        """
        self.log_info(f"selecting value: {value} from dropdown: {locator_name}")
        Select(self.driver.find_element(*locator)).select_by_value(str(value))

    def select_by_index(self, locator, index, locator_name=""):
        self.log_info(f"selecting index: {index} from dropdown: {locator_name}")
        Select(self.driver.find_element(*locator)).select_by_index(index)

    def wait_visible(self, locator, locator_name=""):
        self.log_info(f"wait until element not visible: {locator_name} ")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def take_screenshot(self, name):
        """
        captures screenshot and stores it with timestamp.
        :argument:
            USERNAME_INPUT (str): Screenshot file base USERNAME_INPUT.
         """
        path = f"Screenshots/{name}_{int(time.time())}.png"
        self.driver.save_screenshot(path)
        self.log_info(f"take a screenshot and save to: {path}")

    def switch_to_new_window(self):
        parent = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break

    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.log_info(f"switch to parent window")

    def scroll_to_element(self, locator, locator_name=""):
        self.log_info(f"move to element: {locator_name}")
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_clickable(self, locator, locator_name=""):
        self.log_info(f"wait until element not clickable: {locator_name}")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def safe_action(self, action_name, locator, action, value=None):
        try:
            element = self.driver.find_element(*locator)
            if action == "click":
                element.click()
            elif action == "send_keys":
                element.send_keys(value)

        except Exception as e:
            self.take_screenshot(action_name)
            raise

    def wait_for_alert(self, timeout=5):
        """
        waits for alert popup to appear.
        :argument
            timeout (int): Max wait time in seconds.
        :returns
            bool: True if alert appears, else False.
        """
        self.logger.info("Waiting for alert to be present")
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            self.logger.error("Alert did not appear")
            return False

    def close_google_vignette_ad(self, timeout=2):
        """Universal Google ad killer – never fails test"""

        self.driver.switch_to.default_content()

        try:
            iframes = self.driver.find_elements(By.TAG_NAME, "iframe")

            for frame in iframes:
                try:
                    self.driver.switch_to.frame(frame)

                    # Find ANY possible close button
                    close_btns = self.driver.find_elements(
                        By.XPATH,
                        "//*[contains(@aria-label,'close') or contains(@id,'dismiss') or text()='Close' or text()='close']"
                    )

                    for btn in close_btns:
                        try:
                            # Try normal click
                            if btn.is_displayed():
                                btn.click()
                            else:
                                # Fallback JS click
                                self.driver.execute_script("arguments[0].click();", btn)

                            self.log_info("Ad closed")
                            self.driver.switch_to.default_content()
                            return

                        except ElementNotInteractableException:
                            # JS click fallback
                            self.driver.execute_script("arguments[0].click();", btn)
                            self.log_info("Ad closed via JS")
                            self.driver.switch_to.default_content()
                            return

                        except Exception:
                            continue

                    self.driver.switch_to.default_content()

                except Exception:
                    self.driver.switch_to.default_content()
                    continue

        except Exception:
            pass

        self.driver.switch_to.default_content()
        self.log_info("No ad present — continuing test")
