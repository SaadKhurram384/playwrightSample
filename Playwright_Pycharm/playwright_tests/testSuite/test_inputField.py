import time
import pytest
import json
from playwright.sync_api import Playwright, sync_playwright, expect

# ----------------------------------------------------------------------------------------------------------------

from playwright_tests.functions.navigations.baseURL import *
baseURL = BaseURL()
from playwright_tests.functions.navigations.tabNavigation import *
nav = tabNav()

# ----------------------------------------------------------------------------------------------------------------

@pytest.fixture(scope="session", autouse=True)
def setup_playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function", autouse=True)
def page(setup_playwright):
    base_url = BaseURL()
    page, context, browser = base_url.base_url(setup_playwright)
    yield page
    context.close()
    browser.close()

class TestClass:

    def test_inputText(self, page) -> None:
        page = nav.navigate(route="Text Input", page=page)
        assert page.title() == "Text Input"
        input = page.get_by_placeholder("MyButton")
        buttonText = "Update button text"
        input.type(buttonText, delay=100)
        btn = '//*[@id="updatingButton"]'
        page.click(btn)
        updatedButton_text = page.inner_text('#updatingButton')
        assert buttonText == updatedButton_text
        page.close()

