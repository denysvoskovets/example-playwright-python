from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.continue_button = page.locator('[data-qa="continue-button"]')

    def navigate_to_home(self):
        self.continue_button.click()
