from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest

class Purchase(unittest.TestCase):

    def purchase_test(self):
        base_url = "http://automationpractice.com/index.php"
        driver = webdriver.Firefox()
        action = ActionChains(driver)
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element_by_class_name("login").click()
        driver.find_element_by_id("email").send_keys("newuser123@test.com")
        driver.find_element_by_id("passwd").send_keys("test1")
        driver.find_element_by_id("SubmitLogin").click()

        driver.find_element_by_xpath(".//a[@title='Women']").click()
        driver.execute_script("window.scrollBy(0, 300);")
        first_item = driver.find_element_by_xpath(".//ul[@class='product_list grid row']/li[1]/div")
        action.move_to_element(first_item).perform()
        driver.find_element_by_xpath(".//a[@data-id-product='1']/span[text()='Add to cart']").click()

        time.sleep(3)
        driver.find_element_by_xpath(".//span[contains(text(), 'Proceed to checkout')]").click()

        driver.find_element_by_xpath(".//span[text()='Proceed to checkout']").click()
        driver.find_element_by_xpath(".//span[text()='Proceed to checkout']").click()
        driver.find_element_by_id("cgv").click()
        time.sleep(3)
        driver.find_element_by_xpath(".//button[@name='processCarrier']").click()

        driver.find_element_by_xpath(".//a[@title='Pay by bank wire']").click()
        driver.find_element_by_xpath(".//span[text()='I confirm my order']").click()

        try:
            self.assertTrue(driver.find_element_by_xpath(".//span[text()='Order confirmation']").is_displayed())
            print("assertion good")
        except:
            print("assertion bad")



        driver.quit()


purchase_test = Purchase()
purchase_test.purchase_test()