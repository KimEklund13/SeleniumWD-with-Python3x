from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class CreateAccountTests():

    def CreateAccountTest(self):
        driver = webdriver.Firefox()
        base_url = "http://automationpractice.com/index.php"
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element_by_class_name("login").click()
        driver.find_element_by_id("email_create").send_keys("test+" + str(time.time()) + "@test.com")
        driver.find_element_by_id("SubmitCreate").click()
        driver.find_element_by_id("id_gender2").click()
        driver.find_element_by_id("customer_firstname").send_keys("Kim")
        driver.find_element_by_id("customer_lastname").send_keys("Eklund")
        driver.find_element_by_id("passwd").send_keys("test1")
        day_dropdown = driver.find_element_by_id("days")
        Select(day_dropdown).select_by_value("1")
        month_dropdown = driver.find_element_by_id("months")
        Select(month_dropdown).select_by_value("1")
        year_dropdown = driver.find_element_by_id("years")
        Select(year_dropdown).select_by_value("1985")

        # Scroll down
        driver.execute_script("window.scrollBy(0, 800);")

        driver.find_element_by_id("address1").send_keys("555 fake st")
        driver.find_element_by_id("city").send_keys("Austin")
        state = driver.find_element_by_id("id_state")
        Select(state).select_by_visible_text("Texas")
        driver.find_element_by_id("postcode").send_keys("78758")
        driver.find_element_by_id("phone").send_keys("8055555555")
        driver.find_element_by_id("alias").send_keys("home")

        driver.find_element_by_id("submitAccount").click()

        account_header = driver.title

        try:
            assert account_header == "My account - My Store"
            print("test successful")
        except:
            print("Header not found. Header found was: " + account_header)


create_account_test = CreateAccountTests()
create_account_test.CreateAccountTest()