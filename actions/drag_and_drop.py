from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class DragAndDrop():

    def test(self):
        base_url = "https://jqueryui.com/droppable"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)

        from_element = driver.find_element_by_id("draggable")
        to_element = driver.find_element_by_id("droppable")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(from_element, to_element).perform()
            actions.click_and_hold(from_element).move_to_element(to_element).release().perform()
            print("Drag and drop element successful")
            time.sleep(2)
        except:
            print("Drag and drop failed on element")

ff = DragAndDrop()
ff.test()
