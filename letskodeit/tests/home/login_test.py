from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        base_url = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(base_url)

        login_page = LoginPage(driver)
        login_page.login("test@email.com", "abcabc")



        user_icon = driver.find_element(By.XPATH, "//div[@id='navbar']//a[contains(text(),'My Courses')]")
        if user_icon is not None:
            print("login successful")
        else:
            print("login failed")

        driver.quit()
