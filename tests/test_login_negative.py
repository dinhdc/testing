import pytest

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


class TestNegativeScenario:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUsername", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page._open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"
