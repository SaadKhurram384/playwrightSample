import json

class DynamicButtonPlacement:
    def DynamicButton(self, page):
        with open('../objects/xpaths/xpaths.json', 'r') as a:
            data = json.load(a)
        dynamicButtonXpath = data["PlacementChangeButtonID"]
        try:
            button = page.query_selector(dynamicButtonXpath)
            if button:
                print("Button Found")
                return dynamicButtonXpath
        except Exception as e:
            raise AssertionError(f"Error finding button: {e}")

