from selenium.webdriver.common.by import By

class HandyWrappers():

    # Basically deconstructing the selenium
    # self.driver.find_element(By.typeHere, "value")
    # and shortening it for usage in the 'using_wrappers_demo1.py'

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):  # By which type you want to find the element (ID, Xpath, CSS..)
        # This method gets the By type (.ID, .XPATH, .CLASS) etc.
        # The return on this is used for the next getElement method
        locatorType = locatorType.lower()  # convert to lower case
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "linktext":
            return By.LINK_TEXT
        elif locatorType == "classname":
            return By.CLASS_NAME
        else:
            print("Locator type not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        # This method is called in the test file
        element = None
        try:
            # Building the new method to use
            # byType calls the getByType method, and provides the argument to that method
            byType = self.getByType(locatorType)
            # The element variable ties it all in
            element = self.driver.find_element(byType, locator)
            print("element found")
        except:
            print("element not found")
        return element

    def isElementPresent(self, locator, byType):
        # another way to do the same thing
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("element found")
                return True
            else:
                return False
        except:
            print("element not found")
            return False

    def elementListChecker(self, locator, byType):
        try:
            elementsList = self.driver.find_elements(byType, locator)
            if len(elementsList) > 0:
                print("At least one element in the list was found")
                return True
            else:
                return False
        except:
            print("element not found")
            return False
