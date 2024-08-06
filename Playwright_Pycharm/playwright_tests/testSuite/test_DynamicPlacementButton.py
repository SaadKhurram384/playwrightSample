import time
import pytest
import json
from playwright.sync_api import Playwright, sync_playwright, expect

# ----------------------------------------------------------------------------------------------------------------

from playwright_tests.functions.navigations.baseURL import *
baseURL = BaseURL()
from playwright_tests.functions.navigations.tabNavigation import *
nav = tabNav()
from playwright_tests.functions.Get_Dynamic_Button_Placement import *
placement = DynamicButtonPlacement()

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

    def test_findDynamicButton(self, page) -> None:
        page = nav.navigate(route="Class Attribute", page=page)
        assert page.title() == "Class Attribute"
        response = placement.DynamicButton(page)
        page.click(response)
        page.close()
