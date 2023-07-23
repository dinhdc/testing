from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)

driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)

username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Password123")

btn_locator = driver.find_element(By.ID, "submit")
btn_locator.click()

time.sleep(2)

actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert logout_button_locator.is_displayed()
