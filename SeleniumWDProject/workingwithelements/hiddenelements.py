from selenium import webdriver
import time

class HiddenElements():

    def test(self):
        driver = webdriver.Firefox()
        base_url = "https://learn.letskodeit.com/p/practice"
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        #Find the state of the text box
        textBoxElement = driver.find_element_by_id("displayed-text")
        textBoxState = textBoxElement.is_displayed()
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the hide button
        driver.find_element_by_id("hide-textbox").click()

        # Find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)


        # click the show button
        driver.find_element_by_id("show-textbox").click()

        # find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # browser close
        driver.quit()


    def testExpedia(self):
        # This no longer works, the site has changed the UI
        driver = webdriver.Firefox()
        base_url = "https://www.expedia.com"
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        driver.find_element_by_id("tab-flight-tab").click()

        drpdownElement = driver.find_element_by_id("flight-age-select-1")
        print("Element visible? " + str(drpdownElement.is_displayed()))


ff = HiddenElements()
ff.test()
# ff.testExpedia()