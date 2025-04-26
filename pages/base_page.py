from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import setup_logger
from config.environment import Environment

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Environment.IMPLICIT_WAIT)
        self.logger = setup_logger()

    def find_element(self, locator, timeout=None):
        """Find element with explicit wait"""
        try:
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            self.logger.debug(f"Found element: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            raise

    def find_elements(self, locator, timeout=None):
        """Find multiple elements with explicit wait"""
        try:
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located(locator))
            self.logger.debug(f"Found {len(elements)} elements: {locator}")
            return elements
        except TimeoutException:
            self.logger.error(f"Elements not found: {locator}")
            raise

    def click_element(self, locator, timeout=None):
        """Click element with explicit wait"""
        try:
            element = self.find_element(locator, timeout)
            element.click()
            self.logger.debug(f"Clicked element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to click element: {locator}")
            raise

    def enter_text(self, locator, text, timeout=None):
        """Enter text in element with explicit wait"""
        try:
            element = self.find_element(locator, timeout)
            element.clear()
            element.send_keys(text)
            self.logger.debug(f"Entered text '{text}' in element: {locator}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter text in element: {locator}")
            raise

    def get_text(self, locator, timeout=None):
        """Get text from element with explicit wait"""
        try:
            element = self.find_element(locator, timeout)
            text = element.text
            self.logger.debug(f"Got text '{text}' from element: {locator}")
            return text
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to get text from element: {locator}")
            raise

    def is_element_visible(self, locator, timeout=None):
        """Check if element is visible with explicit wait"""
        try:
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            self.logger.debug(f"Element is visible: {locator}")
            return True
        except TimeoutException:
            self.logger.debug(f"Element is not visible: {locator}")
            return False

    def wait_for_url_contains(self, partial_url, timeout=None):
        """Wait for URL to contain specific text"""
        try:
            wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            wait.until(EC.url_contains(partial_url))
            self.logger.debug(f"URL contains: {partial_url}")
            return True
        except TimeoutException:
            self.logger.error(f"URL does not contain: {partial_url}")
            return False 