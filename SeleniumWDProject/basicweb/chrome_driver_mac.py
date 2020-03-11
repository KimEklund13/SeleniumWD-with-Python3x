from selenium import webdriver

class ChromeDriverMac():

    def test(self):
        # Instantiates the Chrome driver
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")

cc = ChromeDriverMac()
cc.test()