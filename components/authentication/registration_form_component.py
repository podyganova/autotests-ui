from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        # Локаторы элементов страницы Input(page, 'login-form-email-input', 'Email')
        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

    def check_visible(self):
        self.email_input.check_visible()
        self.username_input.check_visible()
        self.password_input.check_visible()

    # Метод для заполнения формы регистрации
    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)  # Проверяем, что email введен корректно
        self.username_input.fill(username)
        self.username_input.check_have_value(username)
        self.password_input.fill(password)
        self.password_input.check_have_value(password)  # Проверяем, что пароль введен корректно
