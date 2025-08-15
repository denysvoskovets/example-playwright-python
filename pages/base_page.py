from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        with allure.step(f'Opening the url {url}'):
            self.page.goto(url, wait_until="domcontentloaded")

    def reload(self):
        with allure.step(f'Opening the url {self.page.url}'):
            self.page.reload(wait_until="domcontentloaded")
