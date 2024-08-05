import json
import pytest

class GetButtonID:
    def Get_Button_ID(self, page, className):
        with open('../objects/xpaths/xpaths.json', 'r') as a:
            data = json.load(a)
        buttonID = data["HiddenLayersID"]
        #classNamestr = str(className)
        completeButtonID = buttonID + className + " ')]"
        #print(f"Complete URL: {completeButtonID}")
        page.wait_for_selector(completeButtonID)

        #Evaluate the ID of the button
        button_id = page.evaluate('''(xpath) => {
                const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                return element ? element.id : null;
            }''', completeButtonID)
        if button_id:
            print(f'The ID of the button is: {button_id}')
            return button_id
        else:
            #print('Button not found')
            pytest.fail("Button not found")

