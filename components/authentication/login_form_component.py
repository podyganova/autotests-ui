import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы элементов страницы
        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(
            page, 'login-page-wrong-email-or-password-alert', 'Wrong email or password'
        )

    @allure.step("Check visible login form")
    def check_visible(self):
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.login_button.check_visible()

    @allure.step("Fill login form")
    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email) # Проверяем, что email введен корректно

        self.password_input.fill(password)
        self.password_input.check_have_value(password)  # Проверяем, что пароль введен корректно
