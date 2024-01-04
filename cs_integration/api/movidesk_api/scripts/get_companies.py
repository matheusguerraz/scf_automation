import requests
import json


# Função para listar todas as empresas no sistema Movidesk
def get_movidesk_companies(token):
    url = "https://api.movidesk.com/public/v1/persons"
    perfil_empresa = 1  # Altere conforme necessário
    params = {
        'token': token,
        '$filter': f'personType eq {perfil_empresa}'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        try:
            data = json.loads(response.text)
            return data
        except json.JSONDecodeError:
            print("Erro ao decodificar a resposta JSON.")
            print(f"Resposta da API: {response.text}")
            return None
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None