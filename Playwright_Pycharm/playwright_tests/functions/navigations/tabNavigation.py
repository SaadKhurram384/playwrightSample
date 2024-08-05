from playwright.sync_api import Playwright, sync_playwright, expect
class tabNav:
    def navigate(self, route, page):
        link = str(route)
        page.get_by_role("link", name=link).click()
        return page