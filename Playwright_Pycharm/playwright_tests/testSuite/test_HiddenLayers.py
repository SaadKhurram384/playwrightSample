import time
import pytest
import json
from playwright.sync_api import Playwright, sync_playwright, expect

# ----------------------------------------------------------------------------------------------------------------

from playwright_tests.functions.navigations.baseURL import *
baseURL = BaseURL()
from playwright_tests.functions.navigations.tabNavigation import *
nav = tabNav()
from playwright_tests.functions.Get_ButtonID import *
buttonID = GetButtonID()

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

    def test_hiddenLayers(self, page) -> None:
        page = nav.navigate(route="Hidden Layers", page=page)
        assert page.title() == "Hidden Layers"
        button_id = buttonID.Get_Button_ID(page, className=' btn-success')
        if button_id == "greenButton":
            page.click('//*[@id="greenButton"]')

        button_idNew = buttonID.Get_Button_ID(page, className=' btn-primary')
        if button_idNew != "greenButton":
            print("No click to be performed on blue button")
        page.close()

