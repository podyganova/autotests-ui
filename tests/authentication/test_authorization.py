import pytest
import allure
from allure_commons.types import Severity
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute
from config import settings


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.xdist_group(name="authorization-group")
    @pytest.mark.parametrize("email, password", [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ])
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)

        login_page.login_form_component.check_visible()
        login_page.login_form_component.fill_login_form(email=email, password=password)
        login_page.login_form_component.login_button.click()

        # Проверяем наличие сообщения об ошибке
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with correct email and password")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self, login_page: LoginPage, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        # Переход на страницу регистрации
        registration_page.visit(AppRoute.REGISTRATION)
        # Заполнение формы регистрации и нажатие кнопки "Registration"
        registration_page.registration_form_component.fill_registration_form(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password)
        registration_page.registration_form_component.registration_button.click()
        # Проверка видимости элементов Dashboard
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
        # Клик по кнопке "Logout"
        dashboard_page.sidebar.click_logout()
        login_page.login_form_component.fill_login_form(
            email=settings.test_user.email, password=settings.test_user.password)
        login_page.login_form_component.login_button.click()
        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar.check_visible(settings.test_user.username)
        dashboard_page.sidebar.check_visible()
