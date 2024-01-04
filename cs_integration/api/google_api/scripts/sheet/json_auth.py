import os

PROJECT_ID = os.environ['PROJECT_ID']
PRIVATE_KEY_ID = os.environ['PRIVATE_KEY_ID']
PRIVATE_KEY = os.environ['PRIVATE_KEY']
CLIENT_EMAIL = os.environ['CLIENT_EMAIL']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_X509_CERT_URL = os.environ['CLIENT_X509_CERT_URL']

credentials_data = {
    "type": "service_account",
    "project_id": PROJECT_ID,
    "private_key_id": PRIVATE_KEY_ID,
    "private_key": PRIVATE_KEY.replace('\\n', '\n'),
    "client_email": CLIENT_EMAIL,
    "client_id": CLIENT_ID,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": CLIENT_X509_CERT_URL,
    "universe_domain": "googleapis.com"
}