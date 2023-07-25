from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "submit")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _open(self):
        self._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        self._click(self.__submit_button)
