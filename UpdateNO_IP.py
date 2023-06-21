#######################################################
# Nome do Arquivo: UpdateNO_IP.py
# Autor: William Amaral de Souza
# Data de Criação: 21/06/2023
# Versao: x.x.x
# Data Modificacao: dd/mm/aa
# Descrição: 
#######################################################
import os
import requests
from datetime import datetime

USUARIO = "EmailDoLogin@gmail.com"
PASSWORD = "SenhaDoLogin"

# Nome do Host ativo
HOST = "exemplodehost.zapto.org"

# Sem necessidade de alteracao
LOG = "/tmp/noip.log"
LOG_IP = "/tmp/ip_atual"

if not os.path.exists(LOG_IP):
    open(LOG_IP, "w").close()

with open(LOG_IP, "r") as ip_file:
    IP_OLD = ip_file.read().strip()

USERAGENT = "Simple Python No-IP Updater/0.1"
BUSCA_IP = requests.get("http://ipecho.net/plain").text.strip()

if BUSCA_IP != IP_OLD:
    with open(LOG, "a") as log_file:
        log_file.write(f"Executando o update do IP {datetime.now().strftime('%d/%m/%Y-%H:%M')}\n")
        url = f"https://dynupdate.no-ip.com/nic/update?hostname={HOST}&myip={BUSCA_IP}"
        response = requests.get(url, headers={"User-Agent": USERAGENT}, auth=(USUARIO, PASSWORD))
        log_file.write(response.text + "\n")
    with open(LOG_IP, "w") as ip_file:
        ip_file.write(BUSCA_IP)
else:
    with open(LOG, "a") as log_file:
        log_file.write(f"Sem necessidade de atualizacao: {datetime.now().strftime('%d/%m/%Y-%H:%M')}\n")
