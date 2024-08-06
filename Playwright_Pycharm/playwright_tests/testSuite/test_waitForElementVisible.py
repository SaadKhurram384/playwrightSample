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

    def test_ajaxRequest(self, page) -> None:
        page = nav.navigate(route="AJAX Data", page=page)
        assert page.title() == "AJAX Data"
        btn = '//*[@id="ajaxButton"]'
        page.click(btn)
        selector = '//*[@id="content"]/p'
        page.wait_for_selector(selector, state="visible")
        page.close()
