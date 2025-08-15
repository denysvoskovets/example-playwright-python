import pytest
import allure

@pytest.mark.regression
class TestProduct:

    @allure.title('Search product')
    def test_search_product(self, home_page, product_page):
        product_name_to_search = 'Stylish'
        home_page.navigate()
        home_page.navbar.click_products()
        product_page.search_product(product_name_to_search)

        product_page.product_title.check_contain_text(product_name_to_search)


    @pytest.mark.smoke
    @allure.title('Add product to cart')
    def test_add_product_to_cart(self, home_page, product_page):
        product_name_to_search = 'Stylish'
        home_page.navigate()
        home_page.navbar.click_products()
        product_page.search_product(product_name_to_search)
        product_page.add_to_cart()

        product_page.add_cart_button.check_visible()
