import json
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

    def test_inputText(playwright: Playwright, gotoWebsite):
        #page = gotoWebsite
        gotoWebsite.get_by_role("link", name="Text Input").click()
        #page.get_by_label("Set New Button Name").highlight()

        input = gotoWebsite.get_by_placeholder("MyButton")
        buttonText = "Update button text"
        input.type(buttonText, delay=100)

        btn = '//*[@id="updatingButton"]'
        gotoWebsite.click(btn)

        updatedButton_text = gotoWebsite.inner_text('#updatingButton')
        assert buttonText == updatedButton_text

        #time.sleep(5)
        return gotoWebsite
