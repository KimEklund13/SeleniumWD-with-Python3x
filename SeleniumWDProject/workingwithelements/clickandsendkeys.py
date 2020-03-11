from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        userEmail = driver.find_element(By.ID, "user_email")
        userEmail.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("password")

        time.sleep(3)  # just added this to slow down selenium so we can watch the test.

        userEmail.clear()  # clears the email text field

        time.sleep(3)

        userEmail.send_keys("test")

        time.sleep(3)

        driver.quit()

ff = ClickAndSendKeys()
ff.test()