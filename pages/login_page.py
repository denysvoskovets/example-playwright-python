import allure

from components.navbar_component import NavbarComponent
from elements.input import Input
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    URL = "https://www.automationexercise.com/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.login_email_input = Input(page, 'input[data-qa="login-email"]', 'Email')
        self.login_password_input = Input(page, 'input[data-qa="login-password"]', 'Password')
        self.login_btn = Button(page, '[data-qa="login-button"]', 'Login')
        self.login_error = Label(page, '//p[text()="Your email or password is incorrect!"]', 'Error')
        self.register_name_input = Input(page, 'input[data-qa="signup-name"]', 'Register name')
        self.register_email_input = Input(page, 'input[data-qa="signup-email"]', 'Register email')
        self.register_button = Input(page, '[data-qa="signup-button"]', 'Register')

    def navigate(self):
        super().navigate(self.URL)

    def fill_login_form(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_email_input.check_have_value(email)

        self.login_password_input.fill(password)
        self.login_password_input.check_have_value(password)

    def click_login_button(self):
        self.login_btn.click()

    def click_registration_button(self):
        self.register_button.click()

    def fill_registration_form(self, name: str, email: str):
        self.register_name_input.fill(name)
        self.register_name_input.check_have_value(email)

        self.register_email_input.fill(email)
        self.register_email_input.check_have_value(email)

    @allure.step('Check visible wrong email or password alert')
    def check_visible_wrong_email(self):
        self.login_error.check_visible()
        self.login_error.check_have_text('Your email or password is incorrect!')

    def start_register(self, name, email):
        self.register_name_input.fill(name)
        self.register_email_input.fill(email)
        self.register_button.click()
