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
        print("abriu")
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["language"]["xpath"].click())
        print("lingua")

    # def language(self):

    def click_on_cookie(self):
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["cookie"]["xpath"].click())
        print("cliclou")

    def pick_better_upgrade(self):
        found = False
        atual_upgrade = 2

        while not found:
            object = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(atual_upgrade))
            object_class = self.driver.find_element_by_xpath(object).get_atribute("class")

            if not "enable" in object_class:
                found = True
            else:
                atual_upgrade += 1
        return atual_upgrade -1

    def buy_upgrade(self):
        object = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.pick_better_upgrade()))
        self.driver.find_element_by_xpath(object).click()


cookie = CookieClicker()
cookie.open_site()

i = 0

while True:
    if i % 500 == 0 and i !=0:
        time.sleep(1)
        cookie.buy_upgrade()
        time.sleep(1)
    cookie.click_on_cookie()
    i+=1