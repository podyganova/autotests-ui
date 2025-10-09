import pytest
from playwright.sync_api import Playwright, Page


# Регистрация нового пользователя и сохранение состояния браузера
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> Page:
    # Запуск браузера
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохранить состояние браузера
    page.context.storage_state(path="browser-state.json")

    yield browser.new_page()
    browser.close()

# Открыть новую страницу браузера, используя сохраненное состояние
@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = initialize_browser_state.context.browser.new_context(storage_state="browser-state.json")
    yield browser.new_page()
