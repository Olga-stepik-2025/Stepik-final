import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage


# ===== ТЕСТЫ ДЛЯ ГОСТЕЙ =====

class TestGuestAddToBasketFromProductPage:
 """Тесты добавления товара в корзину для гостей"""

 def test_guest_cant_see_success_message(self, browser):
  """
  Гость не видит сообщение об успехе при открытии страницы товара
  (БЕЗ добавления в корзину)
  """
  url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

  print(f"\n{'=' * 70}")
  print("🔍 Test: Guest can't see success message (without adding)")
  print(f"{'=' * 70}\n")

  page = ProductPage(browser, url)
  page.open()
  print("✅ Step 1: Product page opened")

  page.should_not_be_success_message()
  print("✅ Step 2: Success message is NOT present (correct!)\n")

 @pytest.mark.xfail(reason="Success message appears after adding to basket")
 def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
  """
  Гость не видит сообщение об успехе ПОСЛЕ добавления товара
  (С добавлением в корзину) - ОЖИДАЕМ ПАДЕНИЕ
  """
  url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

  print(f"\n{'=' * 70}")
  print("🔍 Test: Guest can't see success message (after adding)")
  print(f"{'=' * 70}\n")

  page = ProductPage(browser, url)
  page.open()
  print("✅ Step 1: Product page opened")

  page.add_product_to_basket()
  print("✅ Step 2: Product added to basket")

  page.should_not_be_success_message()
  print("✅ Step 3: Success message is NOT present\n")

 @pytest.mark.xfail(reason="Success message does not disappear after adding to basket")
 def test_message_disappeared_after_adding_product_to_basket(self, browser):
  """
  Сообщение об успехе исчезает после добавления товара в корзину
  (ОЖИДАЕМ ПАДЕНИЕ - сообщение НЕ исчезает)
  """
  url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

  print(f"\n{'=' * 70}")
  print("🔍 Test: Success message disappeared after adding product")
  print(f"{'=' * 70}\n")

  page = ProductPage(browser, url)
  page.open()
  print("✅ Step 1: Product page opened")

  page.add_product_to_basket()
  print("✅ Step 2: Product added to basket")

  print("⏳ Step 3: Checking that success message disappeared...")
  page.should_be_disappeared_success_message()
  print("✅ Step 3: Success message disappeared (as expected)\n")

 @pytest.mark.parametrize('link', [
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
               marks=pytest.mark.xfail(reason="Known bug - name mismatch")),
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
 ])
 def test_guest_can_add_product_to_basket(self, browser, link):
  """Параметризованный тест добавления товара в корзину для гостя"""
  offer_number = link.split("promo=")[1]

  page = ProductPage(browser, link)
  page.open()
  page.should_be_add_to_basket_button()

  product_name = page.get_product_name()
  product_price = page.get_product_price()

  print(f"\n🔍 Testing {offer_number}")
  print(f"📦 Product: {product_name}")
  print(f"💰 Price: {product_price}")

  page.add_product_to_basket()
  page.solve_quiz_and_get_code()
  page.should_be_success_message_with_product_name(product_name)
  page.should_be_basket_total_with_price(product_price)

  print(f"✅ {offer_number} - PASSED\n")


# ===== ТЕСТЫ ДЛЯ ЗАРЕГИСТРИРОВАННЫХ ПОЛЬЗОВАТЕЛЕЙ =====

class TestUserAddToBasketFromProductPage:
 """Тесты добавления товара в корзину для зарегистрированных пользователей"""

 @pytest.fixture
 def setup(self, browser):
  """
  Подготовка к тестам: регистрация нового пользователя
  """
  print(f"\n{'=' * 70}")
  print("🔐 SETUP: Registering new user")
  print(f"{'=' * 70}\n")

  # Генерируем уникальный email для каждого теста
  import uuid
  unique_email = f"user_{uuid.uuid4()}@example.com"
  password = "TestPassword123!"

  # Открываем страницу логина
  login_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
  login_page = LoginPage(browser, login_url)
  login_page.open()
  print("✅ Step 1: Login page opened")

  # Регистрируем пользователя
  login_page.register_new_user(unique_email, password)
  print(f"✅ Step 2: User registered successfully")

  # Проверяем, что пользователь залогинен
  login_page.should_be_authorized_user()
  print(f"✅ Step 3: User is authorized (icon-user present)\n")

  return browser

 def test_user_cant_see_success_message(self, browser, setup):
  """
  Зарегистрированный пользователь не видит сообщение об успехе
  при открытии страницы товара (без добавления в корзину)
  """
  url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

  print(f"\n{'=' * 70}")
  print("🔍 Test: User can't see success message (without adding)")
  print(f"{'=' * 70}\n")

  page = ProductPage(browser, url)
  page.open()
  print("✅ Step 1: Product page opened")

  page.should_not_be_success_message()
  print("✅ Step 2: Success message is NOT present (correct!)\n")

 def test_user_can_add_product_to_basket(self, browser, setup):
  """
  Зарегистрированный пользователь добавляет товар в корзину
  """
  url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

  print(f"\n{'=' * 70}")
  print("🔍 Test: User can add product to basket")
  print(f"{'=' * 70}\n")

  page = ProductPage(browser, url)
  page.open()
  page.should_be_add_to_basket_button()
  print("✅ Step 1: Product page opened")

  product_name = page.get_product_name()
  product_price = page.get_product_price()

  print(f"📦 Product: {product_name}")
  print(f"💰 Price: {product_price}")

  page.add_product_to_basket()
  print("✅ Step 2: Product added to basket")

  page.solve_quiz_and_get_code()
  print("✅ Step 3: Quiz solved")

  page.should_be_success_message_with_product_name(product_name)
  print("✅ Step 4: Success message verified")

  page.should_be_basket_total_with_price(product_price)
  print("✅ Step 5: Basket total verified\n")
