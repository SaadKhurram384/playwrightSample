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

    def test_dynamicIDbutton(self, page) -> None:
        buttonID = "//button[@type='button' and contains(@class, 'btn btn-primary') and text()='Button with Dynamic ID']"
        response = nav.navigate(route="Dynamic ID", page=page)
        assert response.title() == 'Dynamic ID'
        response.click(buttonID)
        page.close()

    def test_findDynamicButton(self, page) -> None:
        page = nav.navigate(route="Class Attribute", page=page)
        assert page.title() == "Class Attribute"
        response = placement.DynamicButton(page)
        page.click(response)
        page.close()

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

    def test_inputText(self, page) -> None:
        page = nav.navigate(route="Text Input", page=page)
        assert page.title() == "Text Input"
        input = page.get_by_placeholder("MyButton")
        buttonText = "Update button text"
        input.type(buttonText, delay=100)
        btn = '//*[@id="updatingButton"]'
        page.click(btn)
        updatedButton_text = page.inner_text('#updatingButton')
        assert buttonText == updatedButton_text
        page.close()

    def test_loadDelay(self, page) -> None:
        page = nav.navigate(route="Load Delay", page=page)
        assert page.title() == "Load Delays"
        wait = page.wait_for_load_state("domcontentloaded")
        assert page.title() == "Load Delays"
        obj = "//button[@class='btn btn-primary' and @type='button' and text()='Button Appearing After Delay']"
        page.click(obj)
        page.close()

    def test_scrollBar(self, page) -> None:
        page = nav.navigate(route="Scrollbars", page=page)
        assert page.title() == "Scrollbars"
        btn = '//*[@id="hidingButton"]'
        buttonLocation = page.locator(btn)
        buttonLocation.scroll_into_view_if_needed()
        buttonLocation.click()
        page.close()

    def test_verifyText(self, page) -> None:
        page = nav.navigate(route="Verify Text", page=page)
        assert page.title() == "Verify Text"
        txt = "//span[normalize-space(.)='Welcome UserName!']"
        #page.locator(txt).highlight()
        text = page.locator(txt).text_content()
        print(f"Text: {text}")
        page.close()

    def test_ajaxRequest(self, page) -> None:
        page = nav.navigate(route="AJAX Data", page=page)
        assert page.title() == "AJAX Data"
        btn = '//*[@id="ajaxButton"]'
        page.click(btn)
        selector = '//*[@id="content"]/p'
        page.wait_for_selector(selector, state="visible")
        page.close()