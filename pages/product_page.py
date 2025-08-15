import time

from pages.base_page import BasePage
from elements.input import Input
from elements.button import Button
from elements.label import Label


class ProductPage(BasePage):
    URL = "https://www.automationexercise.com/products"

    def __init__(self, page):
        super().__init__(page)

        self.product_title = Label(page, "div.product-information h2", "Product")
        self.view_cart_button = Button(page, "text=View Cart", "View Cart")
        self.add_cart_button = Button(page, 'button.btn.btn-default.cart', "Add to cart")

        self.search_input = Input(page, "#search_product", "Search")
        self.submit_search_button = Button(page, "#submit_search", "Submit search")
        self.view_product_buttons = Label(page, 'a:has-text("View Product")', "View Product")

    def navigate(self):
        super().navigate(self.URL)

    def open_product(self):
        self.view_product_buttons.nth(0).click()

    def search_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.submit_search_button.click()
        self.open_product()

    def add_to_cart(self):
        self.add_cart_button.click()
