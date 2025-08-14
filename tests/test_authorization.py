import pytest

from pages.login_page import LoginPage


@pytest.mark.authorization
@pytest.mark.regression
class TestAuthorization:

    def test_login(self, login_page: LoginPage):
        login_page.navigate()

        login_page.fill_login_form(email='flamingo@gmail.com', password='123456')
        login_page.click_login_button()

    @pytest.mark.parametrize('user, password', [
        ('someuser@some.some', '123456'),
        ('someuser@some', '123456'),
        ('someuser@some.some', '123'),
    ])
    def test_wrong_email_password(self, login_page: LoginPage, user: str, password: str):
        login_page.navigate()

        login_page.fill_login_form(email=user, password=password)
        login_page.click_login_button()

        login_page.login_error.check_visible()
