from .autentication import load_credentials, authorize_client, sheet_id
import json
from cs_integration.api.circle_api.scripts.create_user import new_user
import os
from .json_auth import autentication_json, credentials_data
  
# Function for open sheet 
def get_sheet_by_id(client, sheet_id):
    try:    
        sheet = client.open_by_key(sheet_id)
        print('abrimos a planilha')
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


def process_people_sheet(sheet):
    # Encontrar o índice das colunas relevantes
    name_column = sheet.find("Nome completo", in_row=1)

    # Lista para armazenar os dados JSON de cada linha
    people_list = []

    if name_column is not None:
        name_column_index = name_column.col
        email_column_index = sheet.find("E-mail", in_row=1).col
        status_column_index = sheet.find("Status", in_row=1).col
        organization_column_index = sheet.find("Organização", in_row=1).col

        # Obtém os valores das colunas relevantes
        values = sheet.get_all_values()

        # Itera sobre as linhas
        for row_index, row in enumerate(values[1:], start=2):
            name = row[name_column_index - 1]
            email = row[email_column_index - 1]
            status = row[status_column_index - 1]
            organization = row[organization_column_index - 1]

            # Verifica se o status é 'NC'
            if status == 'NC':
                # Cria um dicionário com as informações desejadas
                json_data = {
                    'name': name,
                    'username': email,
                    'email': email,
                    'empresa': organization
                }

                # Adiciona o dicionário à lista
                people_list.append(json_data)

        # Cria o JSON final
        final_json = json.dumps(people_list, ensure_ascii=False, indent=2)
        new_users = json.loads(final_json)
        new_user(new_users)
    else:
        print("Coluna 'Nome' não encontrada na aba 'Pessoas'. Verifique o cabeçalho da planilha.")


def main():

    try:
        autentication_json()
        credential = load_credentials(credentials_data)
        
        if credential:
            print(f'credencial válida {credential}')
            # authorize client
            client = authorize_client(credentials_data)

            if client:
                print(f'cliente válido {client}')
                # Obter sheet por ID
                sheet = get_sheet_by_id(client, sheet_id)

                if sheet:
                    print(f'planilha válida')
                    # Iterar sobre cada aba da sheet
                    for window in sheet:
                        print(f'entrou no loop com a janela {window}')
                        process_status(window)

    except Exception as e:
        print(f'Deu erro aqui {e}')