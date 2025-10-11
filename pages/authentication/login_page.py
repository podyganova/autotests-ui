from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Локаторы элементов страницы
        self.login_form_component = LoginFormComponent(page)

    # Метод для проверки отображения алерта с ошибкой
    def check_visible_wrong_email_or_password_alert(self):
        self.login_form_component.wrong_email_or_password_alert.check_visible()
        self.login_form_component.wrong_email_or_password_alert.check_have_text("Wrong email or password")
