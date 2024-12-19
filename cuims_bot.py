from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from PIL import Image
import pytesseract
import requests
import os

from essentials import uid, pwd

class CuimsBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://uims.cuchd.in/')
        student_login = self.driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[1]/div/a')
        student_login.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        login_input = self.driver.find_element(By.XPATH, '//*[@id="txtUserId"]')
        login_input.send_keys(uid)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="btnNext"]')
        next_btn.click()

        sleep(2)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="txtLoginPassword"]')
        password_input.send_keys(pwd)
    
        captcha = self.driver.find_element(By.XPATH, '//*[@id="imgCaptcha"]')
        captcha.screenshot("captcha.png")

        captcha_image = Image.open("captcha.png")
        captcha_text = pytesseract.image_to_string(captcha_image)
        print(captcha_text)

        captcha_input = self.driver.find_element(By.XPATH, '//*[@id="txtcaptcha"]')
        captcha_input.send_keys(captcha_text)
        os.remove("captcha.png")
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="btnLogin"]')
        login_btn.click()


bot = CuimsBot()
bot.login()