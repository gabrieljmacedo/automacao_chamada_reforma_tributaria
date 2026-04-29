# Automação de POST via CSV (Python)

Script em Python para ler um CSV e enviar requisições POST para uma API - Reforma Tributária.

## Estrutura

- automacao_post_csv.py -> Script principal
- dados.csv -> Arquivo de entrada
- requirements.txt -> Dependências

## Configuração

### 1. Instalar dependências

pip install -r requirements.txt

### 2. Configurar variável de ambiente

#### Windows (PowerShell)

setx API_AUTH_KEY "SEU_TOKEN"

#### Linux/Mac

export API_AUTH_KEY="SEU_TOKEN"

## Execução

python automacao_post_csv.py


## Obs

- Cada linha do CSV gera uma requisição POST
- O header usa API Key (`api-auth`)
- O body é montado com base nas colunas do CSV