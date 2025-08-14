import pytest


def test_search_product(home_page, product_page):
    product_name_to_search = 'Stylish'
    home_page.navigate()
    home_page.navbar.click_products()
    product_page.search_product(product_name_to_search)

    product_page.product_title.check_contain_text(product_name_to_search)


@pytest.mark.smoke
def test_add_product_to_cart(home_page, product_page):
    product_name_to_search = 'Stylish'
    home_page.navigate()
    home_page.navbar.click_products()
    product_page.search_product(product_name_to_search)
    product_page.add_to_cart()

    product_page.add_cart_button.check_visible()
