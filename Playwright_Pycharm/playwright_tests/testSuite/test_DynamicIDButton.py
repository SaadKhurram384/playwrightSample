import json
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time

#from playwright_tests.functions.navigations.baseURL import *
#baseurl = baseURL()

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
        page = gotoWebsite.goto("http://www.uitestingplayground.com/")
        print(f"Page: {page} - GotoWebsite: {gotoWebsite}")
        return gotoWebsite

    @pytest.fixture(autouse=True, scope="session")
    def findButton(self, playwright: Playwright):
        with open('../objects/xpaths/xpaths.json', 'r') as a:
            data = json.load(a)
        buttonID = data["ButtonWithDynamicID"]
        return buttonID


    def test_clickDynamicButton(playwright: Playwright, gotoWebsite, findButton) -> None:
        #page = gotoWebsite
        buttonid = findButton
        gotoWebsite.get_by_role("link", name="Dynamic ID").click()
        assert gotoWebsite.title() == 'Dynamic ID'
        #time.sleep(2)
        gotoWebsite.click(buttonid)
        #time.sleep(2)

