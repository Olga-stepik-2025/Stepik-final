import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации и закрытия браузера
    scope="function" означает, что браузер создается для каждого теста
    """

    print("\n✅ Starting browser...")

    # Опции для Chrome
    options = Options()

    # Опция 1: Раскомментируйте для headless режима (без окна браузера)
    # options.add_argument("--headless")

    # Опция 2: Отключаем sandbox (для Linux серверов)
    options.add_argument("--no-sandbox")

    # Опция 3: Отключаем использование dev shm (для Linux серверов)
    options.add_argument("--disable-dev-shm-usage")

    # Опция 4: Отключаем сигнал автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Опция 5: Устанавливаем размер окна
    options.add_argument("--start-maximized")

    # Инициализация Chrome WebDriver
    driver = webdriver.Chrome(options=options)

    # Неявное ожидание (для поиска элементов)
    driver.implicitly_wait(10)

    # Явное ожидание (timeout для явного ожидания)
    driver.set_page_load_timeout(30)

    # Возвращаем браузер в тест
    yield driver

    # Закрытие браузера после теста (выполняется всегда)
    print("\n✅ Closing browser...")
    driver.quit()


@pytest.fixture(scope="session")
def browser_session():
    """
    Альтернативная фикстура для браузера с scope="session"
    Один браузер на все тесты (быстрее, но может быть нестабильнее)
    Используйте, если тесты независимы
    """
    print("\n✅ Starting session browser...")
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    print("\n✅ Closing session browser...")
    driver.quit()


# Хук для вывода информации перед каждым тестом
def pytest_runtest_setup(item):
    """Выполняется перед каждым тестом"""
    print(f"\n{'=' * 60}")
    print(f"📋 Running test: {item.name}")
    print(f"{'=' * 60}")


# Хук для вывода информации после каждого теста
def pytest_runtest_teardown(item, nextitem):
    """Выполняется после каждого теста"""
    print(f"\n{'=' * 60}")
    print(f"✅ Test completed: {item.name}")
    print(f"{'=' * 60}\n")
