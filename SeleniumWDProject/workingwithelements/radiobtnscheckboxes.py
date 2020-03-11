from selenium import webdriver
import time

class RadioButtonsAndCheckboxes():

    def test(self):
        driver = webdriver.Firefox()
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        bmw_radio = driver.find_element_by_id("bmwradio")
        bmw_radio.click()
        time.sleep(2)

        benz_radio = driver.find_element_by_id("benzradio")
        benz_radio.click()
        time.sleep(2)

        bmw_check = driver.find_element_by_id("bmwcheck")
        bmw_check.click()
        time.sleep(2)

        benz_check = driver.find_element_by_id("benzcheck")
        benz_check.click()
        time.sleep(2)

        print("Is BMW Radio button selected? " + str(bmw_radio.is_selected()))
        print("Is Benz Radio button selected? " + str(benz_radio.is_selected()))
        print("Is BMW Checkbox button selected? " + str(bmw_check.is_selected()))
        print("Is Benz Checkbox button selected? " + str(benz_check.is_selected()))

        driver.quit()

ff = RadioButtonsAndCheckboxes()
ff.test()

