from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ExceptionPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_btn_locator = (By.CSS_SELECTOR, "#add_btn")
    __row_1_input_locator = (By.CSS_SELECTOR, "#row1 input")
    __row_1_edit_button = (By.CSS_SELECTOR, "#row1 #edit_btn")
    __row_2_input_locator = (By.CSS_SELECTOR, "#row2 input")
    __row_1_save_button = (By.CSS_SELECTOR, "#row1 #save_btn")
    __row_2_save_button = (By.CSS_SELECTOR, "#row2 #save_btn")
    __confirmation_locator = (By.ID, "confirmation")
    __instructions__locator = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        self._open_url(self.__url)

    def add_second_row(self):
        self._click(self.__add_btn_locator)

    def is_row2_displayed(self) -> bool:
        return self._is_displayed(self.__row_2_input_locator)

    def add_second_food(self, food: str):
        self._type(self.__row_2_input_locator, food)
        self._click(self.__row_2_save_button)

    def get_confirmation_message(self) -> str:
        return self._get_text(self.__confirmation_locator)

    def change_value_of_row_1(self, food: str):
        self._click(self.__row_1_edit_button)
        self._wait_until_element_is_clickable(self.__row_1_input_locator)
        self._clear(self.__row_1_input_locator)
        self._type(self.__row_1_input_locator, food)
        self._click(self.__row_1_save_button)
        self._wait_until_element_is_visible(self.__confirmation_locator, 10)

    def are_instructions_hide(self) -> bool:
        return self._is_hide(self.__instructions__locator)
