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

    def test_detectDynamicColumnCell(playwright: Playwright, gotoWebsite):
        #page = gotoWebsite
        gotoWebsite.get_by_role("link", name="Dynamic Table").click()
        column_headers = gotoWebsite.locator("//div[@role='rowgroup']/div[@role='row'][1]/span[@role='columnheader']")
        column_count = column_headers.count()

        # Find the position of the "CPU" column
        cpu_column_index = -1
        for i in range(column_count):
            if column_headers.nth(i).text_content() == "CPU":
                cpu_column_index = i + 1  # XPath is 1-indexed
                break

        # Check if the CPU column was found
        if cpu_column_index == -1:
            print("CPU column not found")
            return

        # Locate the row that contains "Chrome"
        chrome_row_xpath = "//div[@role='row'][.//span[@role='cell' and text()='Chrome']]"

        # Construct the XPath to find the CPU value within the "Chrome" row
        cpu_value_xpath = f"{chrome_row_xpath}//span[@role='cell'][{cpu_column_index}]"

        # Get the text content of the CPU cell
        cpu_value = gotoWebsite.locator(cpu_value_xpath).text_content()
        print(f"The CPU value for Chrome is: {cpu_value}")

        return cpu_value