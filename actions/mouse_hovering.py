from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class MouseHovering():

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(3)

        element = driver.find_element_by_id("mousehover")

        item_to_click_locator = ".//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse hovered on element")
            time.sleep(2)
            top_link = driver.find_element_by_xpath(item_to_click_locator)
            # top_link.click()
            time.sleep(2)
            actions.move_to_element(top_link).click().perform() # Explicit sleep before this is needed for geckodriver, don't know why
            time.sleep(3)
            print("Item clicked")
        except:
            print("Mouse hover failed on element")

ff = MouseHovering()
ff.test()