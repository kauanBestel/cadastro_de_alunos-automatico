from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select  
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Tenta clicar em 'SENAC' na árvore de diretórios
def clicar_senac(wait, navegador):
    try:
        print("➡️ Tentando localizar e clicar em 'SENAC' na árvore...")
        senac_folder = wait.until(EC.element_to_be_clickable((
            By.XPATH, '//span[contains(@class,"jstree-node")]//span[contains(normalize-space(.), "SENAC")]'
        )))
        navegador.execute_script("arguments[0].scrollIntoView(true);", senac_folder)
        time.sleep(0.2)
        senac_folder.click()
        return True
    except:
        return False
