import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.exception_page import ExceptionPage


class TestExceptionScenario:

    @pytest.mark.exception
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.add_second_row()
        # Verify Row 2 input field is displayed
        assert exception_page.is_row2_displayed(), "Row2 should be displayed, but it is not"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_second_row()

        exception_page.add_second_food("Sushi")

        assert exception_page.get_confirmation_message() == "Row 2 was saved", \
            "Confirmation message should be saved, but it is not"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.change_value_of_row_1("Sushi")
        assert exception_page.get_confirmation_message() == "Row 1 was saved", \
            "Confirmation message should be saved, but it is not"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()

        exception_page.add_second_row()

        assert exception_page.are_instructions_hide(), "Instruction text element should not be displayed"

    @pytest.mark.exception
    @pytest.mark.debug
    @pytest.mark.timeout
    def test_timeout_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()

        exception_page.add_second_row()

        assert exception_page.is_row2_displayed(), "Failed waiting for Row 2 input to be visible"
