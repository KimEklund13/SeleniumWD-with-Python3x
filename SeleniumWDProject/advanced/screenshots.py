from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        base_url = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()

        self.takeScreenshot(driver)

        driver.quit()

    def takeScreenshot(self, driver):
        """
        Takes a screenshot of the current open web page
        :param driver:
        :return:
        """
        file_name = str(round(time.time() * 1000)) + ".png"  # Generates a random file name
        screenshot_directory = "/Users/KimEklund/Desktop/"
        destination_file = screenshot_directory + file_name

        try:
            driver.save_screenshot(destination_file)
            print("Screenshot saved to directory --> :: " + destination_file)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()