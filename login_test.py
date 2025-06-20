import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import os

CHROME_DRIVER_PATH = './drivers/chromedriver'

LOGIN_URL = 'http://localhost:3000/login' 

EMAIL_CSS_SELECTOR = '#kullaniciAdi'
PASSWORD_CSS_SELECTOR = '#sifre'
LOGIN_BUTTON_CSS_SELECTOR = '#root > div > div > div > button' 


class SimpleLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_simple_login_flow(self):
        self.driver.get(LOGIN_URL)


        email_input = self.driver.find_element(By.CSS_SELECTOR, EMAIL_CSS_SELECTOR)
        email_input.send_keys('test_ogrenci') # Kendi e-postanızla değiştirin


        password_input = self.driver.find_element(By.CSS_SELECTOR, PASSWORD_CSS_SELECTOR)
        password_input.send_keys('test_ogrenci') # Kendi şifrenizle değiştirin


        login_button = self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)
        login_button.click()
        

        
        print("Kullanıcı Giriş Testi Tamamlandı.")
        
        time.sleep(30)
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # unittest.TestCase i kalıtmış tüm sınıfları çalıştır demek