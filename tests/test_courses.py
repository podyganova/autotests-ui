import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):  # Создаем тестовую функцию

    # Переходим на страницу Courses
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем, что на странице "Courses" отображается заголовок "Courses"
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверяем, что на странице "Courses" отображается текст блока "There is no results"
    courses_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_results).to_be_visible()
    expect(courses_results).to_have_text("There is no results")

    # Проверяем на странице "Courses" видимость иконки пустого блока
    courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    # Проверяем, что на странице "Courses" отображается текст описания блока
    courses_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description).to_be_visible()
    expect(courses_description).to_have_text("Results from the load test pipeline will be displayed here")