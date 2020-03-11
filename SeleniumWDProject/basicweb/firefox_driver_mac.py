from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Instantiate's the FF browser command
        driver = webdriver.Firefox()
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()

