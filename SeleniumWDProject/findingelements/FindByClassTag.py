from selenium import webdriver

class FindByClassTag():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByClass = driver.find_element_by_class_name("displayed-class")
        elementByClass.send_keys("Testing the element")

        if elementByClass is not None:
            print("We found element by CLASS")

        elementByTag = driver.find_element_by_tag_name("h1")
        text = elementByTag.text

        if elementByTag is not None:
            print("We found element by TAG and the text on element is: " + text)



ff = FindByClassTag()
ff.test()