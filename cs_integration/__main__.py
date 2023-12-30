# __main__.py
import sys
import os
import logging

# Adicione o diretório principal do projeto ao sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from cs_integration.api.google_api.scripts import get_sheet

if __name__ == "__main__":

    logging.basicConfig(filename='execucao_diaria.log', level=logging.INFO)
    logging.info('Início da execução diária.')
# Teste
    try:
        get_sheet.main()
        logging.info('Execução bem-sucedida.')
    except Exception as e:
        logging.error(f'Erro durante a execução: {e}')