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

    nome_folder = alunos.iloc[0]['Folder'].strip()
    xpath_aluno = f'//span[normalize-space(text())="{nome_folder}"]'
    # Debug: Verificar quantos elementos estão presentes imediatamente
    # Aguarda até que o elemento esteja presente e, em seguida, utiliza JavaScript para clicar nele
    arquivo_aluno = wait.until(EC.presence_of_element_located((By.XPATH, xpath_aluno)))
    arquivo_aluno.click()

    nome_role = wait.until(EC.presence_of_element_located((By.XPATH, '//input[list="editlistinput659269"]' )))
    nome_role.click()
    input("Pressione Enter para continuar...")