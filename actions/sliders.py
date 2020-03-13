from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Sliders():

    def test(self):
        base_url = "https://jqueryui.com/slider"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        slider = driver.find_element_by_xpath(".//div[@id='slider']//span")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slider, 100, 0).perform()
            print("Sliding element successful")
            time.sleep(2)
        except:
            print("sliding failed on element")


ff = Sliders()
ff.test()
