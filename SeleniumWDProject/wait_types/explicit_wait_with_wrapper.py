from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from wait_types.explicitWrapper import ExplicitWaitType
# Imports the wrapper class

class ExplicitWaitWithWrapper():

    def test(self):
        base_url = "http://expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        # Initialize the wrapper class and give it the driver for the init
        driver.get(base_url)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("08/01/2020")
        return_date = driver.find_element(By.ID, "flight-returning-hp-flight")
        return_date.click()
        time.sleep(1)
        # Need this because .clear() isn't clearing the field, only appending the new text on top of the default return date
        # So we need Javascript to clear the field
        driver.execute_script("arguments[0].value='';", return_date)
        time.sleep(1)
        # return_date.clear()
        return_date.send_keys("09/01/2020")
        time.sleep(10)
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()

        # A .5 implicit wait is not long enough for this element. Need to implement an explicit wait.
        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)

        driver.quit()

ff = ExplicitWaitWithWrapper()
ff.test()