from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_product_to_basket(self):
        """Добавляет товар в корзину"""
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        return self

    def should_not_be_success_message(self):
        """
        Проверяет, что НЕТ сообщения об успешном добавлении товара
        """
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        return self

    def should_be_disappeared_success_message(self):
        """
        Проверяет, что сообщение об успехе исчезает
        """
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should have"
        return self

    def get_product_name(self):
        """Возвращает название товара"""
        element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return element.text

    def get_product_price(self):
        """Возвращает цену товара"""
        element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return element.text

    def should_be_success_message_with_product_name(self, product_name):
        """Проверяет сообщение об успешном добавлении товара"""

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE)
        )

        success_element = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        message_product_name = success_element.text

        print(f"\n{'=' * 70}")
        print(f"🔍 SUCCESS MESSAGE CHECK:")
        print(f"   Expected product: '{product_name}'")
        print(f"   Message product:  '{message_product_name}'")
        print(f"{'=' * 70}")

        assert product_name == message_product_name, \
            f"\n❌ BUG FOUND! Product name mismatch!\n" \
            f"   Expected: '{product_name}'\n" \
            f"   Got:      '{message_product_name}'\n"

        print(f"   ✅ Names match exactly!\n")
        return self

    def should_be_basket_total_with_price(self, product_price):
        """Проверяет стоимость корзины"""

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.BASKET_TOTAL_MESSAGE)
        )

        basket_element = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE)
        basket_price = basket_element.text

        print(f"\n{'=' * 70}")
        print(f"💰 BASKET TOTAL CHECK:")
        print(f"   Expected price: '{product_price}'")
        print(f"   Basket price:   '{basket_price}'")
        print(f"{'=' * 70}")

        assert product_price == basket_price, \
            f"\n❌ BUG FOUND! Price mismatch!\n" \
            f"   Expected: '{product_price}'\n" \
            f"   Got:      '{basket_price}'\n"

        print(f"   ✅ Prices match exactly!\n")
        return self

    def should_be_add_to_basket_button(self):
        """Проверяет наличие кнопки добавления в корзину"""
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        assert button.is_displayed(), "Add to basket button not found!"
        return self
