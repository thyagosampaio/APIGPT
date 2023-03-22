import pandas as pd

# Lendo a planilha do Excel
excel_file = 'sua_planilha.xlsx'
sheet_name = 'nome_da_aba'  # Altere para o nome da aba que você deseja ler
df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')

# Convertendo o DataFrame em JSON
json_data = df.to_json(orient='records')

print(json_data)




import requests
import json

api_key = "your_api_key"  # Substitua pelo valor da sua chave de API

# Substitua 'json_data' pelos dados JSON que você deseja enviar
# Neste exemplo, estou usando uma string JSON de exemplo
json_data = '{"key": "value"}'

# Crie um texto a partir dos dados JSON
text_to_process = f"Eu tenho alguns dados JSON e gostaria de obter informações relevantes: {json_data}"

# Defina os parâmetros para a API do GPT-3
payload = {
    "prompt": text_to_process,
    "max_tokens": 100
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Envie a solicitação para a API do GPT-3
response = requests.post("https://api.openai.com/v1/engines/davinci-codex/completions", json=payload, headers=headers)

# Verifique o resultado da API
if response.status_code == 200:
    response_data = response.json()
    generated_text = response_data["choices"][0]["text"]
    print("Texto gerado:", generated_text)
else:
    print("Erro na solicitação:", response.status_code)
