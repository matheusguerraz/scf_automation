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
    
    sheet = 'Pessoas'
    if successful_registrations:
        # Encontrar o índice das colunas relevantes
        email_column_index = sheet.find("E-mail", in_row=1).col
        status_column_index = sheet.find("Status", in_row=1).col

        # Obtém os valores das colunas relevantes
        values = sheet.get_all_values()

        # Itera sobre as linhas
        for row_index, row in enumerate(values[1:], start=2):
            email = row[email_column_index - 1]

            # Se o e-mail estiver na lista de registros bem-sucedidos, atualiza o status para 'C'
            if email in successful_registrations:
                sheet.update_cell(row_index, status_column_index, 'C')