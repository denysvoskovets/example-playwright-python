import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, Locator
from typing import Pattern
from elements.button import Button
import re


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.home_button = Button(page, "ul.nav.navbar-nav li a[href='/']", 'Home button')
        self.products_button = Button(page, "ul.nav.navbar-nav li a[href='/products']", 'Product button')
        self.cart_button = Button(page, "ul.nav.navbar-nav li a[href='/view_cart']", 'Cart button')

    @allure.step('Check visible Navigation Bar')
    def check_visible(self):
        self.home_button.check_visible()
        self.home_button.check_have_text(' Home')
        self.products_button.check_visible()
        self.cart_button.check_visible()

    @allure.step('Navigate to products via Navigation bar')
    def click_products(self):
        self.navigate(self.products_button.get_locator(), (re.compile(r".*/products")))

    @allure.step('Navigate to cart via Navigation bar')
    def click_cart(self):
        self.navigate(self.cart_button.get_locator(), (re.compile(r".*/cart")))

    def navigate(self, button: Locator, expected_url: Pattern[str]):
        button.click()
        self.check_current_url(expected_url)
