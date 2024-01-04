from cs_integration.api.circle_api.scripts.create_user import new_user
import json

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
        if new_users is not None:
            successful_registrations = new_user(new_users)
            print(successful_registrations)
            # Após cadastrar, altera o status dos e-mails na planilha
            if successful_registrations:
                update_status_in_sheet(sheet, successful_registrations)

        else:
            print('Não temos usuários para cadastrar.')

    else:
        print("Coluna 'Nome' não encontrada na aba 'Pessoas'. Verifique eventuais alterações na estrutura")


# Função para atualizar o status dos e-mails na planilha
def update_status_in_sheet(sheet, successful_registrations):
    # Obter o índice da coluna de e-mails
    email_column_index = sheet.find("E-mail", in_row=1).col

    for email in successful_registrations:
        # Iterar sobre as linhas da planilha
        for row_index, row in enumerate(sheet.get_all_values()[1:], start=2):
            current_email = row[email_column_index - 1]
            # Verificar se o e-mail atual corresponde ao e-mail na lista
            if current_email == email:
                # Atualizar o status para 'C' (ou o valor desejado)
                sheet.update_cell(row_index, email_column_index, 'C')
                print(f'Status do e-mail {email} atualizado para "C"')
                break  # Parar a busca após encontrar a correspondência