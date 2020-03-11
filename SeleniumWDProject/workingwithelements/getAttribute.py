from selenium import webdriver
import time


class GetAttribute():

    def test(self):
        base_url = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("class")
        resultid = element.get_attribute("id")

        print("Value of class attribute is: " + result + " ...Value of id attribute is: " + resultid)
        time.sleep(1)

        driver.quit()



ff = GetAttribute()
ff.test()