import requests
from .autentication import get_token
import logging

token = get_token()
successful_registrations = []

def new_user(new_users):

    url = "https://developer.scaffoldplatform.com.br/api/v1/users/new_user"
    for user in new_users:
        payload = user
        headers = {
        'Authorization': f'Bearer {token["access_token"]}',
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            successful_registrations.append(user['email'])

        else:
            user_error = user['name']
            logging.error(f'Tivemos um erro durante o cadastro do {user_error}')


from cs_integration.api.google_api.scripts.get_sheet import register_registered  # Movido para o final
register_registered(successful_registrations)