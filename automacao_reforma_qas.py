from dotenv import load_dotenv 
import csv
import os
import requests
import time

load_dotenv()

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://bus-prd.oxxobr.com.br/szi/api/loadItemReforma/"

API_KEY = os.getenv("API_AUTH_KEY")

HEADERS = {
    "Content-Type": "application/json",
    "api-auth": API_KEY
}

ARQUIVO_CSV = "mercadorias.csv"

def ler_csv(arquivo):
    dados = []
    with open(arquivo, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for linha in reader:
            dados.append(linha)
    return dados

def enviar_post(valor):
    body = {
        "valores": valor
    }

    response = requests.post(
        URL,
        json=body,
        headers=HEADERS,
        timeout=30,
        verify=False
    )

    return response.status_code, response.text

def main():
    registros = ler_csv(ARQUIVO_CSV)

    for linha in registros:
        valor = linha["valores"]
        print(f"➡️ Enviando: {valor}")

        try:
            status, resposta = enviar_post(linha)
            print(f"📡 Status Code: {status}")

        except Exception as e:
            print(f"❌ Erro ao enviar {valor}: {e}")

        print("-" * 60)

        time.sleep(15)  # CONTROLE DE TAXA Oracle NoSQL limita isso a 4 operações por minuto

if __name__ == "__main__":
    main()
