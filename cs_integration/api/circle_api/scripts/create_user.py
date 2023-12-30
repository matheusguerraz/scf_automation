import requests
from .autentication import get_token

token = get_token()

def new_user(new_users):

    url = "https://developer.scaffoldplatform.com.br/api/v1/users/new_user"
    for user in new_users:
        payload = user
        headers = {
        'Authorization': f'Bearer {token["access_token"]}',
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(url, headers=headers, data=payload)

        print(f'Realizamos o cadastro do cara')