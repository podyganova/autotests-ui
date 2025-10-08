from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()

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
    Registration_button = page.get_by_test_id('registration-page-registration-button')
    Registration_button.click()

    # Сохранить состояние браузера
    context.storage_state(path="browser-state.json")

    # Создать новую сессию браузера
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    # Переходим на страницу Courses
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем, что на странице "Courses" отображается заголовок "Courses"
    Courses_page = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(Courses_page).to_be_visible()
    expect(Courses_page).to_have_text("Courses")

    # Проверяем, что на странице "Courses" отображается текст блока "There is no results"
    Courses_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(Courses_results).to_be_visible()
    expect(Courses_results).to_have_text("There is no results")

    # Проверяем на странице "Courses" видимость иконки пустого блока
    Courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(Courses_icon).to_be_visible()

    # Проверяем, что на странице "Courses" отображается текст описания блока
    Courses_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(Courses_description).to_be_visible()
    expect(Courses_description).to_have_text("Results from the load test pipeline will be displayed here")

    # Задержка для наглядности выполнения теста
    page.wait_for_timeout(5000)