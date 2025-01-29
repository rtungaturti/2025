import pytest
from playwright.sync_api import sync_playwright

class PlaywrightLocators:
    USERNAME_INPUT = '#username'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#submit'

class ExamplePagePlaywright:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill(PlaywrightLocators.USERNAME_INPUT, username)
        self.page.fill(PlaywrightLocators.PASSWORD_INPUT, password)
        self.page.click(PlaywrightLocators.LOGIN_BUTTON)

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

def test_login(browser):
    browser.goto("https://practicetestautomation.com/practice-test-login/")
    example_page = ExamplePagePlaywright(browser)
    example_page.login("student", "Password1234")
    print("Hi")
    # Add assertions to verify login success
    assert "Logged In Successfully" in browser.content()  # Use correct Playwright command

if __name__ == "__main__":
    pytest.main(['-v', '--alluredir=playwright_report'])
