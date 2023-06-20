import re
import sys
import time
import shutil
from bs4 import BeautifulSoup
from selenium import webdriver
from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Shopee_Login():
    def __init__(self):
        self.config = dotenv_values("Userdata.env")
        self.username = self.config['USERNAME']
        self.password = self.config['PASSWORD']
        self.remove = r"[\n() ]"
        self.remove_1 = '7-ELEVEN'
        self.remove_2 = '蝦皮海外 - 7-11'
        self.url = 'https://shopee.tw'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.f = open('cargo.txt', 'w', encoding='utf-8')

    def login(self):
        self.driver.get(f'{self.url}/buyer/login')
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'pDzPRp')))
        element = self.driver.find_element(By.NAME, 'loginKey')
        element.send_keys(self.username)
        element = self.driver.find_element(By.NAME, 'password')
        element.send_keys(self.password)
        time.sleep(1)
        button = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button')
        button.click()
        self.get_cargo_data()

    def get_cargo_data(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'stardust-popover')))
        self.driver.get(f'{self.url}/user/purchase/?type=8')
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_20hgQK')))
        time.sleep(1)
        data = self.driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        unprocessed_data = soup.find(class_='fSW3m4').text
        data = re.sub(self.remove, "", str(unprocessed_data))
        print('待收貨:', data)
        data = soup.find_all(class_='KmBIg2')
        self.handle_cargo_data(data)

    def handle_cargo_data(self, data):
        time.sleep(1.5)
        for item in data:
            from etracking import ECTRACKER
            self.driver.get(self.url + item['href'])
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'PW9gQm')))
            data = self.driver.page_source
            soup = BeautifulSoup(data, 'html.parser')
            unprocessed_data_1 = soup.find(class_='g5X7+k').text
            unprocessed_data_2 = unprocessed_data_1.replace(self.remove_1, "")
            data = unprocessed_data_2.replace(self.remove_2, "")
            cargo = ECTRACKER.tracker(data, autoVerify=True)
            del sys.modules['etracking']
            shutil.rmtree('__pycache__')
            self.f.write(str(cargo))
            self.f.write('\n')


SHOPEE_LOGIN = Shopee_Login()
SHOPEE_LOGIN.login()
print('貨態於 <cargo.txt> ')
