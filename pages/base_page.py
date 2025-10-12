import allure
from playwright.sync_api import Page


class BasePage:
    # Конструктор класса, принимающий объект Page
    def __init__(self, page: Page): 
        self.page = page  # Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # Метод для открытия ссылок
        with allure.step(f'Opening the url "{url}"'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            self.page.reload(wait_until='domcontentloaded')
