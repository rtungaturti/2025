import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner

class SeleniumLocators:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")

class ExamplePageSelenium:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*SeleniumLocators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*SeleniumLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*SeleniumLocators.LOGIN_BUTTON).click()

class TestExamplePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.page = ExamplePageSelenium(self.driver)

    def test_login(self):
        self.page.login("student", "Password123")
        # Add assertions to verify login success
        assert "Logged In Successfully" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='selenium_report'))
