# __main__.py
import sys
import os

# Adicione o diretório principal do projeto ao sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from cs_integration.api.google_api.scripts import get_sheet

if __name__ == "__main__":
    get_sheet.main()  # Supondo que existe uma função chamada main no seu script get_sheet.py
