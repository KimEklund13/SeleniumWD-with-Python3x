from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        base_url = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Find departing field
        departing_field = driver.find_element_by_id("flight-departing-hp-flight")
        departing_field.click()
        # Find the date to be selected
        date_to_select = driver.find_element(By.XPATH,
                                             "//div[@class='datepicker-cal-month'][position()=1]//button[@data-day='31']")
        # Click the date
        date_to_select.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        base_url = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Click departing field
        driver.find_element_by_id("flight-departing-hp-flight").click()
        cal_month = driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        all_valid_dates = cal_month.find_elements(By.XPATH, "//button[@class='datepicker-cal-date']")

        for date in all_valid_dates:
            if date.get_attribute("data-day") == "31":
                date.click()
                break
                # When you click an element in this loop, you need to break
                # because all other elements would become stale after you click the desired element



ff = CalendarSelection()
ff.test2()
