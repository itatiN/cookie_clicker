from selenium import webdriver
import time

class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://orteil.dashnet.org/cookieclicker/"
        self.SITE_MAP = {
            "buttons": {
                "language":{
                    "xpath": "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]"
                },
                "cookie": {
                    "xpath": "/html/body/div[2]/div[2]/div[15]/div[8]/button"
                }
                }
            }

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.maximize_window()
    
    def open_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)
        language()

    def language(self):
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["language"]["xpath"].click())

    def click_on_cookie(self):
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["cookie"]["xpath"].click())

    def pick_better_upgrade(self):
        pass

    def buy_upgrade(self):
        pass

cookie = CookieClicker()
cookie.open_site()