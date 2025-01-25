import requests
import pandas as pd
import time

# função para verificar se o CEP é único usando a API ViaCEP
def check_cep_unique(cep):
    cep = cep.strip()  # Remove espaços do CEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('erro', False):  # Se 'erro' for true, não é um CEP único
                return "Não"
            else:  # Caso contrário, é um CEP único
                return "Sim"
        else:
            return "Erro na API"
    except Exception as e:
        return "Erro na Conexão"

# Carrego a planilha
file_path = './CidadesDoBrasil.xlsx' ##Mude conforme necessário
df = pd.read_excel(file_path, sheet_name='Planilha1')

# Aplico a função para verificar os CEPs, com delay entre as requisições
cep_unico_results = []
for cep in df['CEP_INICIAL'].astype(str):
    print(cep)
    result = check_cep_unique(cep)
    cep_unico_results.append(result)
    print(result)
    time.sleep(10)  # Adiciono um delay de 10 segundos entre as requisições para evitar bloqueios

# Adiciono os resultados à planilha
df['CEP_UNICO'] = cep_unico_results

# Salvo os resultados em uma nova planilha
output_path = './ceps_analisados.xlsx'
df.to_excel(output_path, index=False)

print(f"Análise concluída. Resultados salvos em: {output_path}")
