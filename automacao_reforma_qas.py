import csv
import os
import time
import requests
import urllib3
from dotenv import load_dotenv 


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://bus-prd.oxxobr.com.br/szi/api/loadItemReforma/"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
ARQUIVO_CSV = os.path.join(BASE_DIR, "mercadorias.csv")

load_dotenv(dotenv_path=ENV_PATH)

API_KEY = os.getenv("API_AUTH_KEY")
if not API_KEY:
    raise RuntimeError("API_AUTH_KEY não encontrada no .env. Verifique se o arquivo .env existe e contém API_AUTH_KEY=<valor>")

print("API_KEY:", API_KEY)

HEADERS = {
    "Content-Type": "application/json",
    "api-auth": API_KEY
}

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
        verify=False # SSL Off
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
