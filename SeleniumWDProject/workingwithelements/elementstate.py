from selenium import webdriver

class ElementState():

    def test(self):
        driver = webdriver.Firefox()
        baseURL = "http://www.google.com"
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_xpath("//input[@class='gLFyf gsfi']")
        element_state = e1.is_enabled()  # True for enabled, False for disabled
        print("element is enabled: " + str(element_state))
        e1.send_keys("let kode it")

        driver.quit()

ff = ElementState()
ff.test()