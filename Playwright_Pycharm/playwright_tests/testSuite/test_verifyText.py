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
        #NewPage = page.keyboard.press('Shift+Control+N')
        return openBrowser

    @pytest.fixture(autouse=True, scope="session")
    def gotoWebsite(self, playwright: Playwright, openBrowser):
        gotoWebsite = openBrowser
        gotoWebsite.goto("http://www.uitestingplayground.com/")
        return gotoWebsite

    def test_verifyText(playwright: Playwright, gotoWebsite):
        #page = gotoWebsite
        txt = "//span[normalize-space(.)='Welcome UserName!']"
        gotoWebsite.get_by_role("link", name="Verify Text").click()
        gotoWebsite.locator(txt).highlight()
        text = gotoWebsite.locator(txt).text_content()
        print(f"Text: {text}")
        #time.sleep(5)
        return gotoWebsite

