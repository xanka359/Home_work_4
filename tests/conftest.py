from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def manage_browser():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 6.0

    yield
    browser.quit()