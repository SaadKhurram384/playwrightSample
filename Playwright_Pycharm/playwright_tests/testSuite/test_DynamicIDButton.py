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

    def test_dynamicIDbutton(self, page) -> None:
        buttonID = "//button[@type='button' and contains(@class, 'btn btn-primary') and text()='Button with Dynamic ID']"
        response = nav.navigate(route="Dynamic ID", page=page)
        assert response.title() == 'Dynamic ID'
        response.click(buttonID)
        page.close()
