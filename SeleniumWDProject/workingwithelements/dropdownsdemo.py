from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class Dropdownsdemo():

    def test(self):
        driver = webdriver.Firefox()
        base_url = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        select = Select(element)

        select.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        select.select_by_index("2")
        print("Select honda by index")
        time.sleep(2)

        select.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        select.select_by_index(2)
        print("Select Honda by index")

        driver.quit()

ff = Dropdownsdemo()
ff.test()

