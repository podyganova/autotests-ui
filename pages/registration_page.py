from playwright.sync_api import Page
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form_component = RegistrationFormComponent(page)
