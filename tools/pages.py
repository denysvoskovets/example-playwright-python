import allure
from playwright.sync_api import Playwright, Page
from config import settings


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
                               ) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(storage_state=storage_state)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    context.tracing.stop(path = settings.tracing_dir.joinpath(f'./tracing/{test_name}.zip'))
    browser.close()

    allure.attach.file(settings.tracing_dir.joinpath(f'./tracing/{test_name}.zip'), name='trace', extension='zip')