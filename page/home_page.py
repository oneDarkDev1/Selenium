from .base_page import BasePage
from .locators import AuthLocators, AllPetsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AllPetsPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.driver = driver

    @property
    def images(self):
        return self.driver.find_elements(*AllPetsLocators.images)

    @property
    def names(self):
        return self.driver.find_elements(*AllPetsLocators.names)

    @property
    def descriptions(self):
        return self.driver.find_elements(*AllPetsLocators.descriptions)

    def wait_for_load(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(*locator)) > 0
        )