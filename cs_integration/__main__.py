# __main__.py
import sys
import os
import logging

# Adicione o diretório principal do projeto ao sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from cs_integration.api.google_api.scripts import get_sheet

print(f'PLATFORM_CLIENT_ID: {os.environ.get["PLATFORM-CLIENT-ID"]}')
print(f'PLATFORM_CLIENT_SECRET: {os.environ.get["PLATFORM-CLIENT-SECRET"]}')
print(f'PLATFORM_PASSWORD: {os.environ.get["PLATFORM-PASSWORD"]}')
print(f'PLATFORM_USERNAME: {os.environ.get["PLATFORM-USERNAME"]}')
print(f'SHEET_ID: {os.environ.get["SHEET_ID"]}')
print(f'CREDENTIAL: {os.environ.get["CREDENTIAL"]}')

if __name__ == "__main__":

    logging.basicConfig(filename='execucao_diaria.log', level=logging.INFO)
    logging.info('Início da execução diária.')
# Teste
    try:
        get_sheet.main()
        logging.info('Execução bem-sucedida.')
    except Exception as e:
        logging.error(f'Erro durante a execução: {e}')