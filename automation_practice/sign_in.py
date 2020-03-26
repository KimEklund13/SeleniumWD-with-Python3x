from selenium import webdriver


class SignInTests():

    def sign_in_test(self):
        driver = webdriver.Firefox()
        base_url = "http://automationpractice.com/index.php"
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element_by_class_name("login").click()
        # We don't want hardcoded values for real tests. An initial create account
        # at test run beginning should store a new registered user for the test suite
        driver.find_element_by_id("email").send_keys("newuser123@test.com")
        driver.find_element_by_id("passwd").send_keys("test1")
        driver.find_element_by_id("SubmitLogin").click()

        try:
            assert driver.title == "My account - My Store"
            print("test successful")
        except:
            print("login unsuccessful")

        driver.quit()


create_account_test = SignInTests()
create_account_test.sign_in_test()
