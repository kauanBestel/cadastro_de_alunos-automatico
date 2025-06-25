from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

from add_role import adicionar_role
from add_user import adicionar_usuario

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--disable-web-security")

username = "pnetlab"
userPassword = "@@pn3tl@b##2025"



navegador = webdriver.Chrome(options=chrome_options)

navegador.get("https://pnetlab6.inoutcloud.srv.br/store/public/auth/login/offline?link=https%3A%2F%2Fpnetlab6.inoutcloud.srv.br%2Fstore%2Fpublic%2Fadmin%2Fmain%2Fview&error=&success=")



wait = WebDriverWait(navegador, 15)
username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))
username_field.send_keys(str(username))

wait = WebDriverWait(navegador, 15)
passWord_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Password"]')))
passWord_field.send_keys(str(userPassword))

wait = WebDriverWait(navegador, 15)
loginButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="button btn btn-info"]')))
loginButton.click()

input("aperte algo")
input("aperte algo")
input("aperte algo")
input("aperte algo")