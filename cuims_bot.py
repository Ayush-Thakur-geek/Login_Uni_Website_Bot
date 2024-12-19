from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from secrets import uid, pwd

class CuimsBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://uims.cuchd.in/')
        student_login = bot.driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[1]/div/a')
        student_login.click()
        # for handle in self.driver.window_handles:
        #     self.driver.switch_to.window(handle)
        #     print("Current URL:", self.driver.current_url)
        bot.driver.switch_to.window(bot.driver.window_handles[1])
        login_input = bot.driver.find_element(By.XPATH, '//*[@id="txtUserId"]')
        login_input.send_keys(uid)
        next_btn = bot.driver.find_element(By.XPATH, '//*[@id="btnNext"]')
        next_btn.click()
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            print("Current URL:", self.driver.current_url)

        password_input = bot.driver.find_element(By.XPATH, '//*[@id="txtLoginPassword"]')
        password_input.send_keys(pwd)
        sleep(10)
        login_btn = bot.driver.find_element(By.XPATH, '//*[@id="btnLogin"]')
        login_btn.click()

bot = CuimsBot()
bot.login()
