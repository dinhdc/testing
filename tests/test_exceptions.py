import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptionScenario:

    @pytest.mark.exception
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Select Add button
        add_btn_locator = driver.find_element(
            By.CSS_SELECTOR, "#row1 #add_btn")
        # Click Add button
        add_btn_locator.click()

        # explicitly wait
        wait = WebDriverWait(driver, 10)
        row2_input_locator = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#row2 input")))

        # Verify Row 2 input field is displayed
        assert row2_input_locator.is_displayed(), "Row2 should be displayed, but it is not"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Select Add button
        add_btn_locator = driver.find_element(
            By.CSS_SELECTOR, "#row1 #add_btn")
        # Click Add button
        add_btn_locator.click()

        # Wait for the second row to load
        # explicitly wait
        wait = WebDriverWait(driver, 10)
        row2_input_locator = wait.until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#row2 input")))

        # Type text into the second input field
        row2_input_locator.send_keys("Sushi")

        # Push Save button using locator By.name(“Save”)
        # Verify text saved
        save_btn_locator = driver.find_element(
            By.CSS_SELECTOR, "#row2 #save_btn")
        save_btn_locator.click()

        confirmation_locator = wait.until(
            ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_locator.text
        assert confirmation_message == "Row 2 was saved", "Confirmation message should be saved, but it is not"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        wait = WebDriverWait(driver, 10)

        # Clear input field
        edit_btn_element = driver.find_element(
            By.CSS_SELECTOR, "#row1 #edit_btn")
        edit_btn_element.click()
        # Type text into the input field
        input_field_element = wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, "#row1 input")))
        input_field_element.clear()
        input_field_element.send_keys("Sushi")

        # save button
        row_1_save_button = driver.find_element(
            By.CSS_SELECTOR, "#row1 #save_btn")
        row_1_save_button.click()

        # Verify text changed
        text = input_field_element.get_attribute("value")
        assert text == "Sushi", "Text should be changed, but it is not"

        # Verify confirmation text displayed
        confirmation_locator = wait.until(
            ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_locator.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message should be saved, but it is not"

    @pytest.mark.exception
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        wait = WebDriverWait(driver, 10)

        # Push add button
        row_1_add_btn_element = driver.find_element(
            By.CSS_SELECTOR, "#row1 #add_btn")
        row_1_add_btn_element.click()

        # Verify instruction text element is no longer displayed
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), "Instruction text element should not be displayed")

    @pytest.mark.exception
    @pytest.mark.debug
    @pytest.mark.timeout
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        row_1_add_btn_element = driver.find_element(
            By.CSS_SELECTOR, "#row1 #add_btn")
        row_1_add_btn_element.click()

        wait = WebDriverWait(driver, 6)
        row_2_input_element = wait.until(ec.visibility_of_element_located(
            (By.CSS_SELECTOR, "#row2 input")), "Failed waiting for Row 2 input to be visible")
        assert row_2_input_element.is_displayed()
