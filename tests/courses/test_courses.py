import pytest
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):  # Создаем тестовую функцию

        # Переходим на страницу Courses
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Добавили проверку компонентов Navbar и Sidebar на странице Courses
        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible("username")

        # Проверяем, что на странице "Courses" отображается
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):

        # Переходим на страницу создания Courses
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.navbar.check_visible("username")
        create_course_page.create_course_toolbar_view_component.check_visible(is_create_course_disabled=True)
        create_course_page.create_course_form_component.check_visible(
            title='', description='', estimated_time='', max_score='0', min_score='0')
        create_course_page.create_course_exercises_toolbar_view_component.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        # Создание Course
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill_create_course_form(
            title='Playwright', description='Playwright', estimated_time='2 weeks', max_score='100', min_score='10')
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        # Проверка отображениея
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks")

    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        # Переходим на страницу создания Courses
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # Создание Course
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill_create_course_form(
            title='Playwright', description='Playwright', estimated_time='2 weeks', max_score='100', min_score='10')
        create_course_page.create_course_toolbar_view_component.click_create_course_button()

        # Проверка отображениея
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks")

        # Редактирование Course
        courses_list_page.course_view.menu.click_edit(0)
        create_course_page.create_course_form_component.fill_create_course_form(
            title='Playwright v.2', description='Playwright v.2', estimated_time='4 weeks', max_score='200', min_score='20')
        create_course_page.create_course_toolbar_view_component.click_create_course_button()
        # Проверка отображениея
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright v.2", max_score="200", min_score="20", estimated_time="4 weeks")
