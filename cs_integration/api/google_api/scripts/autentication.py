import gspread
from google.oauth2.service_account import Credentials
import os
import json

json_filename = 'service_account_key.json'

# Leia diretamente o arquivo JSON
with open(json_filename) as json_file:
    credentials_data = json.load(json_file)

sheet_id = os.getenv('SHEET_ID')

def load_credentials(credentials_data):
    try:
        creds = Credentials.from_service_account_info(credentials_data, scopes=['https://www.googleapis.com/auth/spreadsheets'])

        return creds
    except Exception as e:
        print(f'Ocorreu um erro ao carregar as credentials: {e}')
        return None

def authorize_client(credentials_data):
    try:        
        client = gspread.authorize(credentials_data)
        return client
    except Exception as e:
        print(f'Ocorreu um erro ao autorizar o cliente: {e}')
        return None