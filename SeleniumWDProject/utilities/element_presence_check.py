from selenium import webdriver
from utilities.handyWrappers import HandyWrappers
from selenium.webdriver.common.by import By
import time

class ElementPresenceCheck():

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(base_url)

        elementResult = hw.isElementPresent("name", By.ID)
        print(str(elementResult))

        elementResult2 = hw.elementListChecker("//input[@id='name']", By.XPATH)
        print(str(elementResult2))

        driver.quit()

ff = ElementPresenceCheck()
ff.test()