import pytest

from pages.login_page_positive import LoginPageSuccess
from pages.login_page import LoginPage


class TestPositiveScenario:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page._open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoginPageSuccess(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as the expected"
        assert logged_in_page.header == "Logged In Successfully"
        assert logged_in_page.is_logout_button_displayed()
