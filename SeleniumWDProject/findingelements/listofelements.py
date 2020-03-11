from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElements():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length = len(elementListByClassName)

        if elementListByClassName is not None:
            print("Size of the list is: " + str(length))  # Just finding the number of nodes

        elementListByTagName = driver.find_elements(By.TAG_NAME, "h1")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("Size of the list is: " + str(length2))



ff = ListOfElements()
ff.test()