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

    def test_loadDelay(playwright: Playwright, gotoWebsite) -> None:
        #page = gotoWebsite
        gotoWebsite.get_by_role("link", name="Load Delay").click()
        wait = gotoWebsite.wait_for_load_state("domcontentloaded")
        assert gotoWebsite.title() == "Load Delays"
        obj = "//button[@class='btn btn-primary' and @type='button' and text()='Button Appearing After Delay']"
        gotoWebsite.click(obj)

