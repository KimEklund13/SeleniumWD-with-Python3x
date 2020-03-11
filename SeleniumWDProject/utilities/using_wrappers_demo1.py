from selenium import webdriver
from utilities.handyWrappers import HandyWrappers
import time


class UsingWrappers():

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)

        text_field = hw.getElement("name")
        text_field.send_keys("Test")
        time.sleep(2)

        text_field2 = hw.getElement("//*[@id='name']", locatorType="xpath")  # Find same element
        text_field2.clear()


        driver.quit()



ff = UsingWrappers()
ff.test()