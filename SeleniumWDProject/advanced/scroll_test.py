from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollTest():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.implicitly_wait(3)

        # Scroll Down (width, height) in pixels (you scroll down, and page goes up) Inverse controls :)
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(3)

        # Scroll Up (you scroll up, and page goes down)
        driver.execute_script("window.scrollBy(0, -800);")
        time.sleep(3)

        # Scroll Element Into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150);")

        # Native Way to Scroll Element Into View
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view  # returns the location back to the var (left corner from top)
        print("Location: " + str(location))

        driver.quit()



ff = ScrollTest()
ff.test()