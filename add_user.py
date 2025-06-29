from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select  
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

import var_globais

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--disable-web-security")

def adicionar_usuario(wait, alunos, navegador):
    navegador.get("https://pnetlab6.inoutcloud.srv.br/store/public/admin/users/offline")
    wait = WebDriverWait(navegador, 15)

    i = 0
    while i < len(alunos):
        nome_user = alunos.iloc[i]['user'].strip()
        role_user = alunos.iloc[i]['Role'].strip()

        add_user = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div')))
        add_user.click()   
        time.sleep(1)

        nome_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Username"]')))
        nome_input.click()
        nome_input.send_keys(Keys.CONTROL, "a")

        nome_input.send_keys(str(nome_user))

        senha_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Password"]')))
        senha_input.click()
        senha_input.send_keys(Keys.CONTROL, "a")
        senha_input.send_keys(var_globais.SENHA_ALUNOS)

        select_element = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@placeholder="Role"]')))
        select = Select(select_element)
        select.select_by_visible_text(role_user)

        runing_nodes = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Max Running Nodes"]')))
        runing_nodes.click()
        runing_nodes.send_keys(Keys.CONTROL, "a")
        runing_nodes.send_keys("5")

        runing_nodes_lab = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Max Running Nodes per Lab"]')))
        runing_nodes_lab.click()
        runing_nodes_lab.send_keys(Keys.CONTROL,"a")
        runing_nodes_lab.send_keys("5")

        # Clica no botão "Add"
        buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.btn.btn-primary')))
        clicou = False
        for btn in buttons:
            if btn.text.strip() == "Add":
                navegador.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(0.5)
                btn.click()
                print(f"✅ Usuário '--{nome_user}--' adicionado com sucesso!")
                clicou = True
                break

        if not clicou:
            raise Exception("Botão 'Add' não encontrado")

        time.sleep(3)

        i = i + 1
