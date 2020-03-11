from selenium import webdriver
from selenium.webdriver.common.by import By

class ByClass():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found 'id name' element")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("Found xpath element")

        elementByLink = driver.find_element(By.LINK_TEXT, "Login")

        if elementByLink is not None:
            print("Found Link - Login element")

ff = ByClass()
ff.test()