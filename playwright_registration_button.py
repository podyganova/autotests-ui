from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверить, что кнопка "Registration" находится в состоянии disabled
    Registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(Registration_button).to_be_disabled()

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Проверить, что кнопка "Registration" находится в состоянии enabled
    Registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(Registration_button).not_to_be_disabled()

    # Задержка для наглядности выполнения теста
    page.wait_for_timeout(5000)