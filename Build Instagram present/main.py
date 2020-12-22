from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

Chrome_driver_path= r"C:\Users\14014\Desktop\100 days of code course Jupiter note book files\Web development topics\Chrome driver\chromedriver.exe"

SIMILAR_ACCOUNT = "python.hub"
INSTAGRAM_URL = "https://www.instagram.com/"
INSTAGRAM_ACCOUNT = "yeisontech2020@gmail.com"
INSTAGRAM_PASSWORD = "Enmanuel1995695"

class IcreaseFollowers:

    def __init__(self, chrome_path):
        self.driver = webdriver.Chrome(executable_path=Chrome_driver_path)


    def login(self):
        
        self.driver.get(INSTAGRAM_URL)
        sleep(2)
        
        user_name= self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(INSTAGRAM_ACCOUNT)
        sleep(1)
        password_user = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_user.send_keys(INSTAGRAM_PASSWORD)
        sleep(1)
        long_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        long_in.click()
        sleep(2)
        save_user = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        save_user.click()
        sleep(1)
        notification_botton = self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notification_botton.click()
        sleep(1)

    def find_followers(self):
        search_Engine = self.driver.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_Engine.send_keys(SIMILAR_ACCOUNT)
        sleep(2)
        tap_seach = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]/div/span')
        tap_seach.click()
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()







running = True
bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
while running:
    bot.follow()


        

