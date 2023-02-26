from pages.auth_page import AuthPage
from pages.elements import *
from settings import *
import pytest



@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--start-maximized")
    return chrome_options


def test_auth_by_phone_number_positive(selenium):
    # EXP-003 Авторизация пользователя с валидным номером телефона и паролем
    page = AuthPage(selenium)
    page.enter_username(AuthPhone.phone)
    page.enter_pass(AuthPhone.password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'

def test_auth_by_email_positive(selenium):
    # EXP-004 Авторизация пользователя с валидной почтой и паролем
    page = AuthPage(selenium)
    page.enter_username(AuthEmail.email)
    page.enter_pass(AuthEmail.password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'

def test_auth_by_phone_number_negative(selenium):
    # EXP-005 Авторизация пользователя с невалидным телефоном/паролем
    page = AuthPage(selenium)
    page.enter_username(AuthPhone.phone)
    page.enter_pass(InvalidData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el('xpath', '//*[@id="page-right"]/div/div/p').text == 'Неверный логин или пароль'


def test_auth_by_email_nagative(selenium):
    # EXP-006 Авторизация пользователя с невалидной почтой и паролем
    page = AuthPage(selenium)
    page.enter_username(AuthEmail.email)
    page.enter_pass(InvalidData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el(*wrong_log_pass_message).text == 'Неверный логин или пароль'

def test_auth_by_login_positive(selenium):
    # EXP-007 Авторизация пользователя с валидным сочетанием логин/пароль
    page = AuthPage(selenium)
    page.enter_username(AuthLogin.login)
    page.enter_pass(AuthLogin.password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'

def test_auth_by_login_negative(selenium):
    # EXP-008 Авторизация пользователя с невалидным сочетанием логин/пароль
    page = AuthPage(selenium)
    page.enter_username(InvalidData.login)
    page.enter_pass(InvalidData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el('xpath', '//*[@id="page-right"]/div/div/p').text == 'Неверный логин или пароль'

def test_auth_by_login_Cyrillic_negative(selenium):
    # EXP-009 Авторизация пользователя с использованием кириллицы в поле ввода логин/пароль
    page = AuthPage(selenium)
    page.enter_username(CyrillicData.login)
    page.enter_pass(CyrillicData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el('xpath', '//*[@id="page-right"]/div/div/p').text == 'Неверный логин или пароль'

def test_auth_by_login_symbol_negative(selenium):
    # EXP-010 Авторизация пользователя с использованием спецсимволов в поле ввода логин/пароль
    page = AuthPage(selenium)
    page.enter_username(SymbolData.login)
    page.enter_pass(SymbolData.password)
    page.btn_click()

    assert page.get_relative_link() != '/account_b2c/page'
    assert page.find_el('xpath', '//*[@id="page-right"]/div/div/p').text == 'Неверный логин или пароль'


def test_auth_with_Longlens_negative(selenium):
    # EXP-011 Проверка ввода в поля логина и пароля строки длиной >1000 символов
    page = AuthPage(selenium)
    page.enter_username(LongData.login * 250)
    page.enter_pass(LongData.password * 250)
    page.btn_click()

    assert page.find_el(*internal_error_message_text).text == 'Internal Server Error'


def test_forget_password(selenium):
    # EXP-012 Проверка перехода по ссылке "Забыл пароль"
    page = AuthPage(selenium)
    page.forget_password_link.click()

    assert page.find_el(*res_pass_text).text == 'Восстановление пароля'


def test_registration(selenium):
    # EXP-013 Проверка перехода по ссылке "Зарегистрироваться"
    page = AuthPage(selenium)
    page.registration_link.click()

    assert page.find_el(*reg_page_text).text == 'Регистрация'




def test_auth_vk(selenium):
    # EXP-014 Проверка перехода по ссылке авторизации пользователя через VK
    page = AuthPage(selenium)
    page.vk_button.click()

    assert page.get_base_url() == 'oauth.vk.com'


def test_auth_ok(selenium):
    # EXP-015 Проверка перехода по ссылке авторизации пользователя через сайт одноклассники
    page = AuthPage(selenium)
    page.ok_button.click()

    assert page.get_base_url() == 'connect.ok.ru'


def test_auth_mail(selenium):
    # EXP-016 Проверка перехода по ссылке авторизации пользователя через сайт Мой мир
    page = AuthPage(selenium)
    page.mailru_button.click()

    assert page.get_base_url() == 'connect.mail.ru'


def test_auth_google(selenium):
    # EXP-017 Проверка перехода по ссылке авторизации пользователя через Google
    page = AuthPage(selenium)
    page.google_button.click()

    assert page.get_base_url() == 'accounts.google.com'


def test_auth_yandex(selenium):
    # EXP-018 Проверка перехода по ссылке авторизации пользователя через Yandex
    page = AuthPage(selenium)
    page.ya_button.click()

    assert page.get_base_url() == 'oauth.yandex.ru'

