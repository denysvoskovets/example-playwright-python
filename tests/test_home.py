import pytest
import allure

from pages.home_page import HomePage


@pytest.mark.regression
@pytest.mark.home
class TestHome:
    @allure.title('Home page opening')
    def test_home_displaying(self, home_page: HomePage):
        home_page.navigate()
        home_page.navbar.check_visible()
        home_page.check_visible_category()
        home_page.check_visible_features()

        home_page.navbar.click_products()
