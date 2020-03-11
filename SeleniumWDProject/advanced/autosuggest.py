"""
There are scenarios when these kind of elements are difficult to find.
In that case, we will have to perform the action to type the letters which will show the list and then from automation,
we need to print the page source.

Then from the console output we need to look at the page source to find the elements.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoSuggest():

    def test1(self):
        base_url = "http://www.cheapflights.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        # Click departure airport/city input field
        departure = driver.find_element(By.NAME, "origin")
        departure.click()
        departure.send_keys("New York")
        # Find the auto suggest element
        time.sleep(2)  # Give it a sec to open the fly-out list of airports
        # Find the option in the fly-out popup
        airports = driver.find_element(By.XPATH, "//li[@data-apicode='JFK']")
        airports.click()

        driver.quit()

ff = AutoSuggest()
ff.test1()