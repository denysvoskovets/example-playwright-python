import pytest
from playwright.sync_api import Page

from pages.account_created_page import AccountCreatedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)


@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)


@pytest.fixture
def account_created_page(page: Page) -> AccountCreatedPage:
    return AccountCreatedPage(page=page)


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page=page)


@pytest.fixture
def product_page(page_with_state: Page) -> ProductPage:
    return ProductPage(page=page_with_state)
