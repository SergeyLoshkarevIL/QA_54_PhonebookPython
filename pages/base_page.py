import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        logger.info(f"click on {locator}")
        self.find(locator).click()

    def fill(self, locator, value):
        logger.info(f"fill {locator} with {value}")
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, 10).until(
            expected_conditions.alert_is_present()
        )