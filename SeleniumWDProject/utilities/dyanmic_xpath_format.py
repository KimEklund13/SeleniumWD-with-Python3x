from selenium import webdriver
from utilities.handyWrappers import HandyWrappers
from selenium.webdriver.common.by import By

class DynamicXPath():

    def test(self):
        base_url = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(base_url)

        # Login -> Lecture "How to click and type in a web element"
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Search for courses
        search_box = driver.find_element(By.ID, "search-courses")
        search_box.send_keys("Javascript")
        go_search = driver.find_element(By.CLASS_NAME, "fa-search")
        go_search.click()

        # Select Course
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()

        driver.quit()

ff = DynamicXPath()
ff.test()