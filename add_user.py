from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select  
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--disable-web-security")

def adicionar_usuario(wait, alunos, navegador):
        
    navegador.get("https://pnetlab6.inoutcloud.srv.br/store/public/admin/users/offline")

    nome_user = alunos.iloc[0]['user'].strip()
    role_user = alunos.iloc[0]['Role'].strip()

    wait = WebDriverWait(navegador, 15)

    add_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div')))
    add_user.click()   
    time.sleep(1)

    nome_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Username"]')))
    nome_input.click()
    nome_input.send_keys(str(nome_user))

    senha_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Password"]')))
    senha_input.click()
    senha_input.send_keys("123")

    select_element = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//select[@placeholder="Role"]')))
    
    select = Select(select_element)
    select.select_by_visible_text(role_user)

    runing_nodes = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Max Running Nodes"]')))
    runing_nodes.click()
    runing_nodes.send_keys("5")

    runing_nodes_lab = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Max Running Nodes per Lab"]')))
    runing_nodes_lab.click()
    runing_nodes_lab.send_keys("5")

    time.sleep(1)
    add_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(@class, "btn-primary") and normalize-space()="Add"]')))
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_btn)
    time.sleep(0.5)
    navegador.execute_script("arguments[0].click();", add_btn)

    print("aperta algo ai")
    input("press")





