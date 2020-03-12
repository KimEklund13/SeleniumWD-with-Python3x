from selenium import webdriver
import time

class SwitchToFrame():

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        # Scroll down to the iFrame area
        driver.execute_script("window.scrollBy(0, 1000);")

        # Switch to frame using ID
        driver.switch_to.frame("courses-iframe")

        # Switch to frame using name
        #driver.switch_to.frame("iframe-name")

        # Switch to frame using numbers (if there is no ID, Name attributes)
        # Finds iframe in index (if there were multiple iframes in view
        # driver.switch_to.frame(0)


        # Search course
        time.sleep(3)
        search_box = driver.find_element_by_id("search-courses")
        search_box.send_keys("python")
        time.sleep(3)

        # Switch back to the parent handle
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)
        driver.find_element_by_id("name").send_keys("Test successful")

ff = SwitchToFrame()
ff.test()