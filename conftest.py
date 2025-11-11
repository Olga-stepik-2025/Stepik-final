import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Добавляем опцию командной строки --language
    По умолчанию используется английский язык (en)
    """
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Specify language for browser: ru, en, es, fr, etc.'
    )


@pytest.fixture(scope="function")
def browser(request):
    """
    Фикстура для создания браузера с указанным языком
    """
    # Получаем значение параметра language из командной строки
    user_language = request.config.getoption("language")
    
    print(f"\n🌐 Запуск браузера с языком: {user_language}")
    
    # Настройка опций Chrome
    options = Options()
    options.add_experimental_option(
        'prefs', 
        {'intl.accept_languages': user_language}
    )
    
    # Создание экземпляра браузера
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    
    yield browser
    
    # Закрытие браузера после теста
    print(f"\n🛑 Закрытие браузера")
    browser.quit()
