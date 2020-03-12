from selenium import webdriver
import time

class SwitchToWindow():

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_url)

        # Find parent handle -> Main Window
        parent_handle = driver.current_window_handle
        print("Parent handle: " + parent_handle)

        # Find "open window" button and click it
        driver.find_element_by_id("openwindow").click()
        time.sleep(2)

        # Find all handles, there should be two handles after clicking "open window" button
        handles = driver.window_handles

        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print("Switched to window: " + handle)
                search_box = driver.find_element_by_id("search-courses")
                search_box.send_keys("python")
                time.sleep(2)
                driver.close()
                break

        # Switch back to the parent handle
        driver.switch_to.window(parent_handle)
        # Do more actions on the parent window if you want
        driver.find_element_by_id("name").send_keys("test successful")
        time.sleep(3)

        driver.quit()

ff = SwitchToWindow()
ff.test()
