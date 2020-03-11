from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found 'link text' login element")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Logi")  # case sensitive string

        if elementByPartialLinkText is not None:
            print("We found 'partial link text' element")



ff = FindByLinkText()
ff.test()