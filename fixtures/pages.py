import pytest
from playwright.sync_api import Page

from pages.account_created_page import AccountCreatedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


@pytest.fixture
def login_page(chromium_page: Page) -> LoginPage:
    return LoginPage(page=chromium_page)


@pytest.fixture
def registration_page(chromium_page: Page) -> RegistrationPage:
    return RegistrationPage(page=chromium_page)


@pytest.fixture
def account_created_page(chromium_page: Page) -> AccountCreatedPage:
    return AccountCreatedPage(page=chromium_page)


@pytest.fixture
def home_page(chromium_page: Page) -> HomePage:
    return HomePage(page=chromium_page)


@pytest.fixture
def product_page(chromium_page: Page) -> ProductPage:
    return ProductPage(page=chromium_page)
