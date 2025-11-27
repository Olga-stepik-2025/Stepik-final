import math
import time
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открывает страницу"""
        self.browser.get(self.url)
        return self

    def is_element_present(self, how, what):
        """
        Проверяет, что элемент присутствует на странице
        :param how: способ поиска (By.CSS_SELECTOR, By.XPATH и т.д.)
        :param what: локатор элемента
        :return: True если элемент найден, False если нет
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяет, что элемент НЕ появляется на странице в течение заданного времени
        :param how: способ поиска
        :param what: локатор элемента
        :param timeout: время ожидания (по умолчанию 4 секунды)
        :return: True если элемент не появился, False если появился
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет, что элемент исчезает со страницы
        :param how: способ поиска
        :param what: локатор элемента
        :param timeout: время ожидания
        :return: True если элемент исчез, False если остался
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """Переходит на страницу входа"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        return self

    def should_be_authorized_user(self):
        """
        Проверяет, что пользователь залогинен
        """
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"
        return self

    def solve_quiz_and_get_code(self):
        """Решает математическое выражение из alert"""
        try:
            print("⏳ Waiting for alert...")
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())

            alert = self.browser.switch_to.alert
            alert_text = alert.text

            x = alert_text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            print(f"🧮 Calculated answer: {answer}")

            alert.send_keys(answer)
            alert.accept()

            try:
                time.sleep(1)
                alert = self.browser.switch_to.alert
                code = alert.text
                print(f"🎉 Code received: {code}")
                alert.accept()
            except NoAlertPresentException:
                print("ℹ️ No second alert")

        except Exception as e:
            print(f"❌ Error in solve_quiz_and_get_code: {e}")
            raise

        time.sleep(0.5)
        return self
