import requests
from .autentication import get_token
import logging

token = get_token()
successful_registrations = []
error_registrations = []

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
            error_registrations.append(user_error)
            
    if successful_registrations:
        print(f'Tivemos os seguintes usuários cadastrados:\n{successful_registrations}')
    else:
        print('Não tivemos cadastros no dia de hoje.')

    if error_registrations:
        print(f'Tivemos erro no cadastro dos seguintes usuários:\n{error_registrations}')       
    else:
        print('Não tivemos erros para cadastrar usuários')

    return successful_registrations, error_registrations