from playwright.sync_api import Playwright, sync_playwright, expect
import pytest

class launchBrowser:
    def openBrowser(self, playwright: Playwright):
        browser = playwright.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context(no_viewport=True)
        openBrowser = context.new_page()

        return openBrowser