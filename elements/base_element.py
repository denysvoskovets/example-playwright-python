from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator_str = locator

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator_formatted = self.locator_str.format(**kwargs)
        return self.page.locator(locator_formatted).nth(nth)

    def get_locators(self, nth: int = 0, **kwargs) -> list[Locator]:
        locator = self.get_locator(nth, **kwargs)
        return locator.all()

    def nth(self, index: int, **kwargs) -> Locator:
        return self.get_locator(**kwargs).nth(index)

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)

    def check_contain_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_contain_text(text)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)
