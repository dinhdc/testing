from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple, time: int = 10) -> WebElement:
        self._wait_until_element_is_visible(locator, time)
        return self._driver.find_element(locator)

    def _type(self, locator: tuple, value: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._driver.find_element(locator).send_keys(value)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._driver.find_element(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple, time: int):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _open_url(self, url: str):
      self._driver.get(url)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _get_text(self, locator: tuple, time: int = 10) -> str:
      self._wait_until_element_is_visible(locator, time)
      return self._find(locator).text
