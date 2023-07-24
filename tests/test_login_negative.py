import pytest

from selenium.webdriver.common.by import By
import time


class TestNegativeScenario:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUsername", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        time.sleep(5)
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)

        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        btn_locator = driver.find_element(By.ID, "submit")
        btn_locator.click()

        time.sleep(2)

        error_locator = driver.find_element(By.ID, "error")
        assert error_locator.is_displayed(), "Error message is not displayed, but it should be"

        error_message = error_locator.text
        assert error_message == expected_error_message, "Error message is not expected"
