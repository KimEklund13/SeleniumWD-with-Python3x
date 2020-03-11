from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        openTabElement = driver.find_element(By.ID, "opentab")
        element_text = openTabElement.text
        print(element_text)
        time.sleep(1)

        driver.quit()



ff = GetText()
ff.test()