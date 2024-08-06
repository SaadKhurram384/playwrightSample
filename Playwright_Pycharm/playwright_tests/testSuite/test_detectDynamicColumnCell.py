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

    def test_detectDynamicColumnCell(self, page) -> None:
        page = nav.navigate(route="Dynamic Table", page=page)
        assert page.title() == "Dynamic Table"
        column_headers = page.locator("//div[@role='rowgroup']/div[@role='row'][1]/span[@role='columnheader']")
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
        cpu_value = page.locator(cpu_value_xpath).text_content()
        print(f"The CPU value for Chrome is: {cpu_value}")
        page.close()