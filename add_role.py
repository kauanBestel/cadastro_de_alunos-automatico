from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
   
    i = 0
    while i < len(alunos):  

        nome_folder = alunos.iloc[i]['Folder'].strip()
        role_name = alunos.iloc[i]['Role'].strip()

        xpath_aluno = f'//span[normalize-space(text())="{nome_folder}"]'

        print(f"\n🔁 Iteração {i+1}/{len(alunos)} — Processando: {nome_folder}")

    
        add_role = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div')))
        add_role.click()
        time.sleep(1)

        senac_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="SENAC"]')))
        # Espera até o botão "SENAC" estar visível (não clicável ainda)
        senac_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[text()="SENAC"]')))
        print("🔍 Botão 'SENAC' visível, aguardando clique...")
# Agora espera ele estar clicável
        senac_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="SENAC"]')))
        botoes_senac = navegador.find_elements(By.XPATH, '//span[text()="SENAC"]')
        print(f"🔎 Encontrados {len(botoes_senac)} botões com texto 'SENAC'")

        senac_button.click()


        f_path1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(normalize-space(.), "TSC - TESTE - 2025")]')))
        f_path1.click()
        time.sleep(1)


        arquivo_aluno = wait.until(EC.presence_of_element_located((By.XPATH, xpath_aluno)))
        arquivo_aluno.click()

        nome_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.input_item_input[type="text"]')))
        nome_input.click()
        nome_input.send_keys(Keys.CONTROL, "a")
        nome_input.send_keys(str(role_name))

        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Rename or Move Folder"]')))
        checkbox.click()
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Move Lab"]')))
        checkbox.click()
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Rename Lab"]')))
        checkbox.click()

        buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.btn.btn-primary')))
        clicou = False
        for btn in buttons:
            if btn.text.strip() == "Add":
                navegador.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(0.5)
                btn.click()
                print(f"✅ Usuário '--{nome_folder}--' adicionado com sucesso!")
                clicou = True
                break

        if not clicou:
            raise Exception("Botão 'Add' não encontrado")

        time.sleep(2)

        i = i + 1







