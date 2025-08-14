from components.navbar_component import NavbarComponent
from elements.label import Label
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.automationexercise.com/"

    def __init__(self, page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.account_created_label = Label(page, 'h2[data-qa="account-created"]', 'Account created label')
        self.features_section = Label(page, 'div.features_items', 'Features section')
        self.category_section = Label(page, 'div.category-products', 'Category section')

    def navigate(self):
        super().navigate(self.URL)

    def check_visible_features(self):
        self.features_section.check_visible()

    def check_visible_category(self):
        self.category_section.check_visible()
