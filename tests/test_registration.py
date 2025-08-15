import pytest

from playwright.sync_api import expect
from pages.account_created_page import AccountCreatedPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
import allure


@pytest.mark.regression
@pytest.mark.registration
class TestRegistration:

    @allure.title('Register new user')
    @pytest.mark.parametrize("user_data", ["normal", "long_names"], indirect=True)
    def test_register(self, user_data, login_page: LoginPage, registration_page: RegistrationPage,
                      account_created_page: AccountCreatedPage):
        login_page.navigate()
        login_page.start_register(user_data['name'], user_data['email_address'])
        registration_page.register_user(user_data)

        expect(account_created_page.continue_button).to_be_visible()

    @allure.title('Email field is prefilled during registration')
    def test_email_is_prefilled(self, user_data, login_page: LoginPage, registration_page: RegistrationPage):
        login_page.navigate()
        login_page.start_register(user_data['name'], user_data['email_address'])

        expect(registration_page.email_input).to_have_value(user_data['email_address'])
