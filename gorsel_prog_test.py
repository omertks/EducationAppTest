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

OGRENCI_USER_NAME = "enesHekkin"
OGRENCI_SIFRE = "enesHekkin"

OGRETMEN_USER_NAME = "omerKarakartal"
OGRETMEN_SIFRE = "omerKarakartal"

def login(self, username, password):
        self.driver.get(LOGIN_URL)


        email_input = self.driver.find_element(By.CSS_SELECTOR, EMAIL_CSS_SELECTOR)
        email_input.send_keys(username) # Kendi e-postanızla değiştirin


        password_input = self.driver.find_element(By.CSS_SELECTOR, PASSWORD_CSS_SELECTOR)
        password_input.send_keys(password) # Kendi şifrenizle değiştirin


        login_button = self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)
        login_button.click()
        
        time.sleep(1)
def logout(self):
    logout_btn = self.driver.find_element(By.CSS_SELECTOR, "#root > nav > div > button.btn.btn-outline-danger")
    logout_btn.click()
    time.sleep(1)
    

class SimpleLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_simple_login_flow(self):
        
        login(self,OGRETMEN_USER_NAME,OGRETMEN_SIFRE)
        
        sinif_olustur_btn = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div.card-body > div > button")
        sinif_olustur_btn.click()
        
        time.sleep(1)
        
        sinif_adi = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > form > div:nth-child(1) > input")
        sinif_adi.send_keys("test_sinifi")
        
        sinif_kontenjani = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > form > div:nth-child(2) > input")
        sinif_kontenjani.send_keys("12")
        
        time.sleep(1)
        sinif_olustur_btn = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > form > button")
        sinif_olustur_btn.click()
        time.sleep(1)
        
        sinif = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div.card-body > div > div > a")
        sinif.click()
        time.sleep(2)
        
        sinif_kod = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > p:nth-child(3)")

        # Elementin içindeki metni alın
        sinif_kod = sinif_kod.get_attribute("textContent").strip().replace('"', '')
        
        sinif_kod = sinif_kod[5:]
        
        print("Sınıf Kodu kod: " + sinif_kod)
        
        odev_olustur = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > button")
        odev_olustur.click()
        time.sleep(1)
        
        odev_baslik = self.driver.find_element(By.CSS_SELECTOR, "#title")
        odev_baslik.send_keys("Final Ödevi")
        
        odev_aciklama = self.driver.find_element(By.CSS_SELECTOR, "#description")
        odev_aciklama.send_keys("Girilen Sayının Faktoriyelini hesaplayan algoritmayı Çiziniz ?")
        
        odev_tarih = self.driver.find_element(By.CSS_SELECTOR, "#dueDate")
        tarih_saat_degeri = "2025-08-12T10:30"

        # JavaScript ile value'yu ayarlayın ve change olayını tetikleyin
        script = """
            const element = arguments[0];
            const value = arguments[1];
            element.value = value;
            element.dispatchEvent(new Event('change', { 'bubbles': true }));
        """
        self.driver.execute_script(script, odev_tarih, tarih_saat_degeri)

        
        time.sleep(1)
        
        odev_olustur_btn = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        odev_olustur_btn.click()
        
        time.sleep(6)
        
        
        logout(self)
        
        
        login(self,OGRENCI_USER_NAME,OGRENCI_SIFRE)
        
        
        sinifa_katil = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div.col-lg-6.col-md-12.mb-3.mb-lg-0 > div > div.card-body > div > div > input[type=text]")
        sinifa_katil.send_keys(sinif_kod)
        
        
        sinifa_katil_btn = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div:nth-child(2) > div.col-lg-6.col-md-12.mb-3.mb-lg-0 > div > div.card-body > div > div > button.btn.btn-info") 
        sinifa_katil_btn.click()
        
        time.sleep(2)
        
        sinif_ogrenci = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div > div:nth-child(2) > div.col-lg-6.col-md-12.mb-3.mb-lg-0 > div > div.card-body > div > div.list-group > a")
        sinif_ogrenci.click()
        
        time.sleep(2)
        
        odev_goruntule_btn = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div > div > ul:nth-child(7) > li > div > button")
        odev_goruntule_btn.click()
        time.sleep(1)
        
        ice_aktar_btn = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div > div:nth-child(4) > div:nth-child(6) > input")
        ice_aktar_btn.send_keys(os.path.abspath('./answers/faktoriyelDiagrami.json'))
        
        time.sleep(1)
        
        odev_gonder_btn = self.driver.find_element(By.CSS_SELECTOR,"#root > div > button")
        odev_gonder_btn.click()
        
        time.sleep(6)
        
        odev_gonder_geri_btn = self.driver.find_element(By.CSS_SELECTOR,"#backBtn")
        odev_gonder_geri_btn.click()
        
        time.sleep(1)
        
        ogretmene_mesaj_btn = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div > div > button")
        ogretmene_mesaj_btn.click()
        
        time.sleep(1)
        
        ogrenci_message_txt = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div > div > div:nth-child(3) > input")
        ogrenci_message_txt.send_keys("Test Mesajı Sa")
        
        ogrenci_message_send_btn = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div > div > div:nth-child(3) > button")
        ogrenci_message_send_btn.click()
        
        time.sleep(1)
        
        logout(self=self)
        
        login(self,OGRETMEN_USER_NAME,OGRETMEN_SIFRE)
        
        test_sinifi = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div > div:nth-child(2) > div:nth-child(2) > div > div.card-body > div > div > a")
        test_sinifi.click()
        
        print("Görsel Programlama Testi Başarılı.")
        
        time.sleep(7000)
        
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # unittest.TestCase i kalıtmış tüm sınıfları çalıştır demek