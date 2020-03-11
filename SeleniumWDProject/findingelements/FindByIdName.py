from selenium import webdriver

class FindByIdName():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print("We found 'id name' element")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("Found show-hide element")

        driver.get("https://www.yahoo.com")
        yahoo_element = driver.find_element_by_id("header-signin-link")

        if yahoo_element is not None:
            print("Found yahoo element")




ff = FindByIdName()
ff.test()