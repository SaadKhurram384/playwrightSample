from playwright.sync_api import Playwright, sync_playwright, expect

class BaseURL:
    def base_url(self, p: Playwright):
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--start-maximized"]
        )
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto("http://www.uitestingplayground.com/")
        return page, context, browser