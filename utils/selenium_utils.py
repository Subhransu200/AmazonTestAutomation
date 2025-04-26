from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import setup_logger

class SeleniumUtils:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = setup_logger()

    def wait_for_element(self, locator):
        self.logger.debug(f"Waiting for element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        self.logger.debug(f"Waiting for clickable element: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator)) 