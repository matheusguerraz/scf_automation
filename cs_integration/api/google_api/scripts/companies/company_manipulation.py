from cs_integration.api.movidesk_api.scripts.get_companies import get_movidesk_companies
from cs_integration.api.movidesk_api.scripts.create_company import create_movidesk_company
import os

# Função para processar a aba 'Empresas'
def process_companies_sheet(sheet, client):
    # Encontrar o índice das colunas relevantes
    status_column_index = sheet.find("Cadastrado", in_row=1).col

    # Lista para armazenar os dados JSON de cada linha
    companies_list = []

    # Obtém os valores da coluna "Cadastrado"
    status_values = sheet.col_values(status_column_index)

    # Pula a primeira linha, que é geralmente o cabeçalho
    for i, status in enumerate(status_values[1:], start=2):
        if status.lower() == 'não':
            company_data = {
                "isActive": True,
                "personType": 2,
                "corporateName": sheet.cell(i, sheet.find("Razão social", in_row=1).col).value,
                "businessName": sheet.cell(i, sheet.find("Nome fantasia", in_row=1).col).value,
                "businessBranch": sheet.cell(i, sheet.find("Ramo de Atividade", in_row=1).col).value,
                "cpfCnpj": sheet.cell(i, sheet.find("CNPJ", in_row=1).col).value
            }
            companies_list.append(company_data)

    # Obter empresas cadastradas no Movidesk
    token = os.environ['TOKEN_MOVIDESK']
    movidesk_companies = get_movidesk_companies(token)

    # Filtrar empresas não cadastradas
    companies_to_register = [
        company for company in companies_list
        if not is_company_registered(movidesk_companies, company['corporateName'])
    ]

    # Cadastrar empresas no Movidesk
    for company in companies_to_register:
        create_movidesk_company(token=token, payload=company)

# Função para verificar se uma empresa já está cadastrada no sistema Movidesk
def is_company_registered(movidesk_companies, corporate_name):
    for company in movidesk_companies:
        if company.get('corporateName') == corporate_name:
            return True
    return False