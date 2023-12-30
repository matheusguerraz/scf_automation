import requests
import time
import os
from dotenv import load_dotenv


client_id = os.getenv("platform-client_id")
client_secret = os.getenv("platform-client_secret")
username = os.getenv("platform-username")
password = os.getenv("platform-password")


class TokenExpiredException(Exception):
    pass

def get_token():
    if hasattr(get_token, "_cached_token") and not is_token_expired(get_token._cached_token):
        return get_token._cached_token
    else:
        url = "https://developer.scaffoldplatform.com.br/oauth/token"
        payload = {
            'grant_type': 'password',
            'username': username,
            'password': password,
            'client_id': client_id,
            'client_secret': client_secret
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            response_data = response.json()
            get_token._cached_token = response_data  # Armazenar o objeto JSON para reutilização
            return response_data
        else:
            raise Exception("Failed to retrieve access token")

def is_token_expired(token):
    expires_in = token.get("expires_in", 0)
    
    if expires_in > 0:
        created_at = token.get("created_at", 0)

        # Certifique-se de que "created_at" é um número antes de calcular a expiração
        if isinstance(created_at, (int, float)):
            expiration_timestamp = created_at + expires_in
            current_timestamp = time.time()
            return current_timestamp > expiration_timestamp
        else:
            # Se "created_at" não for um número, assumimos que o token está expirado
            return True
    else:
        # Se não houver informações de expiração, assumimos que o token está expirado
        return True

def refresh_token(refresh_token):
    url = "https://developer.scaffoldplatform.com.br/oauth/token"
    payload = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': '45',
        'client_secret': 'e3YJR5NHCP8MD16iEs4M0gPKTr39U5t1hGQO1aUf'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to refresh access token")

# Exemplo de uso
token_response = get_token()
token = token_response["access_token"]
refresh_token_value = token_response["refresh_token"]

# Verificar se o token expirou ou é inválido
if is_token_expired(token_response):
    new_token_response = refresh_token(refresh_token_value)
    new_token = new_token_response["access_token"]
else:
    print("Token válido. Não é necessário atualizar.")
