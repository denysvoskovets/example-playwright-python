from typing import Generator
from config import settings, Browser

import pytest
from playwright.sync_api import Page, Playwright

from pages.login_page import LoginPage
from _pytest.fixtures import SubRequest

from tools.pages import initialize_playwright_page


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.fill_login_form(email=settings.test_user.email, password=settings.test_user.password)
    login_page.click_login_button()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(params=settings.browsers)
def page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Generator[
    Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=settings.browser_state_file
    )
