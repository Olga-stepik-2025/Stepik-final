from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        assert isinstance(super(MainPage, self).__init__, object)
        super(MainPage, self).__init__(*args, **kwargs)

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        except NoSuchElementException:
            raise AssertionError("Login link not found!")
