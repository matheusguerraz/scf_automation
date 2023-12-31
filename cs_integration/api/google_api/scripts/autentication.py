import gspread
from google.oauth2.service_account import Credentials
import os
import json
#teste
with open('service_account_key.json') as json_file:
    credentials = json.load(json_file)

sheet_id = os.getenv('SHEET_ID')

def load_credentials(credentials):
    try:
        creds = Credentials.from_service_account_file(credentials, scopes=['https://www.googleapis.com/auth/spreadsheets'])
        return creds
    except Exception as e:
        print(f'Ocorreu um erro ao carregar as credentials: {e}')
        return None

def authorize_client(credentials):
    try:        
        client = gspread.authorize(credentials)
        return client
    except Exception as e:
        print(f'Ocorreu um erro ao autorizar o cliente: {e}')
        return None