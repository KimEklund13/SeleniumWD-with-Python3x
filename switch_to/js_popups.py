from selenium import webdriver
import time
"""
Test:
Given I am on the practice webpage
When I type "Kim" into the "Enter Your Name" field
And I click the alert button  --> triggers the alert popup
And I click ok on the alert popup
And I type "Kim" into the "Enter Your Name" field
And I click the confirm button --> triggers the confirm popup
And I click cancel on the confirm popup
Then I should see the practice webpage --> (Find an element on the page to assert)
"""

class JavaScriptPopups():

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        driver.find_element_by_id("name").send_keys("Kim")
        driver.find_element_by_id("alertbtn").click()
        time.sleep(3)

        # Switch to alert popup and accept
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(3)

        # Switch to confirm popup and CANCEL to excuse. (.accept = confirm)
        driver.find_element_by_id("name").send_keys("Kim")
        driver.find_element_by_id("confirmbtn").click()
        time.sleep(3)
        alert2 = driver.switch_to.alert
        alert2.dismiss()

        driver.quit()

ff = JavaScriptPopups()
ff.test()
