import gspread
from google.oauth2.service_account import Credentials
import os
import json
import base64

# Carregue as credenciais diretamente do JSON
json_encode = os.environ('CRED_JSON')

credentials_json = base64.b64encode(f'{json_encode}'.encode('ascii'))

credentials_data = json.loads(credentials_json)

sheet_id = os.environ.get('SHEET_ID')

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