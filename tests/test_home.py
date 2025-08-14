import pytest

from pages.home_page import HomePage


@pytest.mark.regression
@pytest.mark.home
class TestHome:
    def test_home_displaying(self, home_page: HomePage):
        home_page.navigate()
        home_page.navbar.check_visible()
        home_page.check_visible_category()
        home_page.check_visible_features()

        home_page.navbar.click_products()
