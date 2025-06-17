from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--disable-web-security")


def adicionar_role(wait, alunos, navegador):

    navegador.get("https://pnetlab6.inoutcloud.srv.br/store/public/admin/user_roles/view")

    nome_folder = alunos.iloc[0]['Folder'].strip()
    xpath_aluno = f'//span[normalize-space(text())="{nome_folder}"]'

    role_name = alunos.iloc[0]['Role'].strip()
  
    wait = WebDriverWait(navegador, 15)
    add_role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div')))
    add_role.click()
    time.sleep(1)

    wait = WebDriverWait(navegador, 15)
    senac_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="SENAC"]')))
    senac_button.click()

    f_path1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(normalize-space(.), "TSC - NOITE - 2025")]')))
    f_path1.click()
    time.sleep(1)



    arquivo_aluno = wait.until(EC.presence_of_element_located((By.XPATH, xpath_aluno)))
    arquivo_aluno.click()

    nome_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.input_item_input[type="text"]')))
    nome_input.click()
    nome_input.send_keys(str(role_name))

    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Rename or Move Folder"]')))
    checkbox.click()
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Move Lab"]')))
    checkbox.click()
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Rename Lab"]')))
    checkbox.click()

    add = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="file_mng_modal1750164689863210"]/div/div/div[2]/div[2]/button[1]')))
    add.click()

    input("terminar programa?")




