from .autentication import load_credentials, authorize_client, sheet_id
from scripts.people.people_manipulation import process_people_sheet
from .json_auth import credentials_data
from scripts.companies.company_manipulation import process_companies_sheet

  
# Function for open sheet 
def get_sheet_by_id(client, sheet_id):
    try:    
        sheet = client.open_by_key(sheet_id)
        return sheet
    except Exception as e:
        print(f'Ocorreu um erro ao abrir a planilha: {e}')
        return None

# Conjunto para armazenar os títulos das abas 'Pessoas' já processadas
processed_people_sheets = set()

def process_status(sheet, status_column_index=1):
    
    # Obtém os valores da coluna "Status"
    status_values = sheet.col_values(status_column_index)

    # Pula a primeira linha, que é geralmente o cabeçalho
    for i, status in enumerate(status_values[1:], start=2):
        if status == 'NC':
            if sheet.title == 'Pessoas' and sheet.title not in processed_people_sheets:
                process_people_sheet(sheet)
                # Adiciona o título da aba 'Pessoas' ao conjunto de abas processadas
                processed_people_sheets.add(sheet.title)

    if sheet.window == 'Empresas':
        process_companies_sheet(sheet)
    
def main(): 
    try:
        credential = load_credentials(credentials_data)
        
        if credential:
            # authorize client
            client = authorize_client(credential)

            if client:
                sheet = get_sheet_by_id(client, sheet_id)

                if sheet:
                    # Iterar sobre cada aba da sheet
                    for window in sheet:
                        process_status(window)

    except Exception as e:
        print(f'Erro no processo de autenticação: {e}')