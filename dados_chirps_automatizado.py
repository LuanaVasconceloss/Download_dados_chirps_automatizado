# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:15:20 2023

@author: luana
"""

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL da página que contém os links de download
url = "https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/by_month/"

# Pasta onde você deseja salvar os arquivos baixados
download_folder = "CHIRPS_data"

# Crie a pasta de download se ela não existir
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Realize uma solicitação HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Use o BeautifulSoup para analisar o conteúdo da página
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre todos os links na página
    links = soup.find_all("a")

    # Itere pelos links e baixe os arquivos que deseja
    for link in links:
        href = link.get("href")
        if href and href.endswith(".nc"):
            file_url = urljoin(url, href)
            file_name = os.path.join(download_folder, os.path.basename(file_url))
            # Verifique se o arquivo já foi baixado
            if not os.path.exists(file_name):
                print(f"Baixando {file_name}...")
                with open(file_name, "wb") as file:
                    file.write(requests.get(file_url).content)
            else:
                print(f"O arquivo {file_name} já existe.")
else:
    print("Erro ao acessar a página:", response.status_code)
