import gspread
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
import os

sheet_id = os.environ['SHEET_ID']

 
def load_credentials(credentials_data):
    try:
        
        creds = service_account.Credentials.from_service_account_file(
            credentials_data,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        return creds
    except Exception as e:
        print(f'Ocorreu um erro ao carregar as credenciais: {e}')
        return None


def authorize_client(credentials_data):
    try:        
        client = gspread.authorize(credentials_data)
        return client
    except Exception as e:
        print(f'Ocorreu um erro ao autorizar o cliente: {e}')
        return None