import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize("email, password", [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        login_page.login_form_component.check_visible()
        login_page.login_form_component.fill_login_form(email=email, password=password)
        login_page.login_form_component.login_button.click()

        # Проверяем наличие сообщения об ошибке
        login_page.check_visible_wrong_email_or_password_alert()

    def test_successful_authorization(
            self, login_page: LoginPage, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        # Переход на страницу регистрации
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        # Заполнение формы регистрации и нажатие кнопки "Registration"
        registration_page.registration_form_component.fill_registration_form(
            email="user.name@gmail.com", username="username", password="password")
        registration_page.registration_form_component.registration_button.click()
        # Проверка видимости элементов Dashboard
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
        # Клик по кнопке "Logout"
        dashboard_page.sidebar.click_logout()
        login_page.login_form_component.fill_login_form(email="user.name@gmail.com", password="password")
        login_page.login_form_component.login_button.click()
        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible("username")
        dashboard_page.sidebar.check_visible()
