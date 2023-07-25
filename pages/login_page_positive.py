from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPageSuccess(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __text_locator = (By.TAG_NAME, "h1")
    __logout_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def get_current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return self._get_text(self.__text_locator)

    @property
    def is_logout_button_displayed(self) -> bool:
        return self.is_displayed(self.__logout_button_locator)
