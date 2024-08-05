import json
import re
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time
import playwright
from playwright_tests.functions.Get_ButtonID import *
buttonID = GetButtonID()

class TestClass:

    @pytest.fixture(autouse=True, scope="session")
    def openBrowser(self, playwright: Playwright):
        browser = playwright.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context(no_viewport=True)
        openBrowser = context.new_page()
        # NewPage = page.keyboard.press('Shift+Control+N')
        return openBrowser

    @pytest.fixture(autouse=True, scope="session")
    def gotoWebsite(self, playwright: Playwright, openBrowser):
        gotoWebsite = openBrowser
        gotoWebsite.goto("http://www.uitestingplayground.com/")
        return gotoWebsite

    def test_ajaxRequest(playwright: Playwright, gotoWebsite):
        #page = gotoWebsite
        gotoWebsite.get_by_role("link", name="AJAX Data").click()
        assert gotoWebsite.title() == "AJAX Data"
        btn = '//*[@id="ajaxButton"]'
        gotoWebsite.click(btn)
        selector = '//*[@id="content"]/p'
        gotoWebsite.wait_for_selector(selector, state="visible")
        return gotoWebsite

