from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input =page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    Registration_button = page.get_by_test_id('registration-page-registration-button')
    Registration_button.click()

    # Проверяем, что на странице "Dashboard" отображается заголовок "Dashboard"
    Dashboard_page = page.get_by_test_id('dashboard-toolbar-title-text')
    #expect(Dashboard_page).to_be_visible()
    expect(Dashboard_page).to_have_text("Dashboard")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)