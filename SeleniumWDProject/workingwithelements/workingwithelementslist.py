from selenium import webdriver
import time

class WorkingWithElementsList():

    def test(self):
        driver = webdriver.Firefox()
        base_url = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        radio_buttons_list = driver.find_elements_by_xpath("//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radio_buttons_list)
        print("size of list: " + str(size))

        for radio_button in radio_buttons_list:
            is_selected = radio_button.is_selected()

            # if statement within the for loop. The click() action iterates over each element in the list
            if not is_selected:   # If radio_button is not "is_selected" (True). This executes if value is False
                radio_button.click()
                time.sleep(2)

        driver.quit()


ff = WorkingWithElementsList()
ff.test()
