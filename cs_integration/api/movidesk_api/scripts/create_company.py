import requests

# Função para cadastrar empresas no sistema Movidesk
def create_movidesk_company(token, payload):
    url = "https://api.movidesk.com/public/v1/persons"
    headers = {
        'Content-Type': 
        'application/json'
        }    

    response = requests.post(url,headers=headers , json=payload)

    if response.status_code == 201:  # 201 indica que a empresa foi criada com sucesso
        print(f"Empresa cadastrada com sucesso: {payload['corporateName']}")
        return True
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return False
    
