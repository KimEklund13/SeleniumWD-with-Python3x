from selenium import webdriver

class SafariDriverMac():

    def test(self):
        # Instantiates Safari Browser Command (no need to specify executable, since its stock on Mac)
        driver = webdriver.Safari()
        driver.get("http://letskodeit.com")

sf = SafariDriverMac()
sf.test()