from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "submit")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _open(self):
        self._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        self._click(self.__submit_button)

    def get_error_message(self) -> str:
        return self._get_text(self.__error_message)
