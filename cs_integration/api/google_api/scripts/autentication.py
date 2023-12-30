import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

dot_env_path = r'C:\Users\usuario\scf-automation\cs_integration\credential\keys\.env'

load_dotenv(dot_env_path)

credential_path = os.environ.get('CRED_JSON')
sheet_id = os.getenv('SHEET_ID')

def load_credentials(credential_path):
    try:
        creds = Credentials.from_service_account_file(credential_path, scopes=['https://www.googleapis.com/auth/spreadsheets'])
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