from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    """Класс для работы со страницей входа/регистрации"""

    def should_be_login_page(self):
        """Проверяет, что мы на странице входа"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        return self

    def should_be_login_url(self):
        """Проверяет URL страницы входа"""
        assert "login" in self.browser.current_url, \
            f"Expected 'login' in URL, got: {self.browser.current_url}"
        return self

    def should_be_login_form(self):
        """Проверяет наличие формы входа"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not present"
        return self

    def should_be_register_form(self):
        """Проверяет наличие формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not present"
        return self

    def register_new_user(self, email, password):
        """
        Регистрирует нового пользователя
        :param email: email для регистрации
        :param password: пароль для регистрации
        """
        print(f"\n{'=' * 70}")
        print(f"📝 Registering new user")
        print(f"   Email: {email}")
        print(f"{'=' * 70}\n")

        # Находим поле email регистрации
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        print(f"✅ Email entered: {email}")

        # Находим поле пароля регистрации
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)
        print(f"✅ Password entered")

        # Находим поле подтверждения пароля
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM)
        password_confirm_field.send_keys(password)
        print(f"✅ Password confirmation entered")

        # Находим и нажимаем кнопку регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        print(f"✅ Registration button clicked")

        # Ждём, пока страница загрузится после регистрации
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(LoginPageLocators.REGISTER_EMAIL)
        )

        import time
        time.sleep(2)

        return self
