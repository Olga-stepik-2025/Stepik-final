from login_page import LoginPage


def test_guest_should_see_login_page(browser):
    """Тест: гость должен видеть страницу логина со всеми элементами"""
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


def test_guest_should_see_login_url(browser):
    """Красный тест: проверяем URL"""
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    """Красный тест: проверяем форму логина"""
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    """Красный тест: проверяем форму регистрации"""
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


def test_guest_should_see_login_inputs(browser):
    """Красный тест: проверяем поля для ввода в форме логина"""
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_username_input()
    page.should_be_login_password_input()
    page.should_be_login_button()


def test_guest_should_see_register_inputs(browser):
    """Красный тест: проверяем поля для ввода в форме регистрации"""
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_username_input()
    page.should_be_register_email_input()
    page.should_be_register_password_input()
    page.should_be_register_password_confirm_input()
    page.should_be_register_button()
