from selenium import webdriver

class BrowserInteraction():

    def test(self):
        baseURL = ("https://letskodeit.teachable.com/pages/practice")
        driver = webdriver.Firefox()

        # Window Maximize - maximize the window before you fetch the website
        driver.maximize_window()

        # Open URL
        driver.get(baseURL)

        # Get title
        title = driver.title
        print("title of the webpage is: " + title)

        # Get current URL
        currentURL = driver.current_url
        print("current url of the web page is: " + currentURL)

        # Browser refresh
        driver.refresh()
        print("Browser refreshed 1st time")

        driver.get(driver.current_url)
        print("Browser refreshed 2nd time")

        # Open another url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_up?reset_purchase_session=1")

        # Browser back
        driver.back()
        print("Go one step back in browser history")

        # Browser forward
        driver.forward()
        print("Go one step forward in browser history")

        # Get page source
        page_source = driver.page_source

        # Browser close/quit
        driver.quit()


ff = BrowserInteraction()
ff.test()