from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():  # Создаем тестовую функцию

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
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохранить состояние браузера
        context.storage_state(path="browser-state.json")

        # Создать новую сессию браузера
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
        page = context.new_page()

        # Переходим на страницу Courses
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем, что на странице "Courses" отображается заголовок "Courses"
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        # Проверяем, что на странице "Courses" отображается текст блока "There is no results"
        courses_results = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_results).to_be_visible()
        expect(courses_results).to_have_text("There is no results")

        # Проверяем на странице "Courses" видимость иконки пустого блока
        courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_icon).to_be_visible()

        # Проверяем, что на странице "Courses" отображается текст описания блока
        courses_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_description).to_be_visible()
        expect(courses_description).to_have_text("Results from the load test pipeline will be displayed here")