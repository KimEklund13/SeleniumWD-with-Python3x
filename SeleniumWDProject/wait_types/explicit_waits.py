from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo():

    def test(self):
        base_url = "http://expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        driver.maximize_window()
        driver.get(base_url)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("08/01/2020")
        return_date = driver.find_element(By.ID, "flight-returning-hp-flight")
        return_date.clear()
        return_date.send_keys("09/01/2020")
        time.sleep(10)
        driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()

        # A .5 implicit wait is not long enough for this element. Need to implement an explicit wait.
        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        non_stop_element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        non_stop_element.click()

        time.sleep(2)

        driver.quit()

ff = ExplicitWaitDemo()
ff.test()