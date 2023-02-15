import requests
import json

def preenche_cnpj(id: int,dicionario : dict):
    """Recebe o ID de uma empresa e um dicionário que contém informações relacinadas ao seu CNPJ e as insere no HubSpot

    Args:
        id (int): ID da empresa no HubSpot
        dicionario (dict): Dicionário com as informações referentes ao seu CNPJ
    """    
    url = f"https://api.hubapi.com/crm/v3/objects/companies/{id}"
    token = "token"

    payload = json.dumps({
        "properties": {
        "cnpj" : dicionario["cnpj"],
        "razao_social": dicionario['nome'],
        "capital_social": dicionario['capital_social'],
        "natureza_juridica": dicionario['natureza_juridica'],
        "endereco__bairro": dicionario['bairro'],
        "endereco__cep": dicionario['cep'],
        "endereco__cidade": dicionario['municipio'],
        "endereco__complemento": dicionario['complemento'],
        "endereco__numero": dicionario['numero'],
        "endereco_brasil": dicionario['logradouro'],
        "endereco__uf": dicionario['uf'],
        "cnae_principal": dicionario["atividade_principal"][0]['text'],
        "atividade_principal": dicionario["atividade_principal"][0]['text'],
        "data_de_fundacao_da_empresa_brasil": dicionario["abertura"],
        "data_eleicao_diretoria_da_empresa_brasil": dicionario['data_situacao'],
        "data_da_ultima_alteracao_da_empresa_brasil": dicionario['ultima_atualizacao']
        }
    })

    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json" 
    }
    requests.patch(url, headers = headers, data=payload)
    return 


if __name__ == "__main__":
    dicionario = {'atividade_principal': [{'code': '63.11-9-00', 'text': 'Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na internet'}], 'data_situacao': '17/11/2021', 'tipo': 'MATRIZ', 'nome': 'KAMINO INSTITUICAO DE PAGAMENTO LTDA', 'abertura': '17/11/2021', 'telefone': '(11) 8168-2441', 'email': 'guto@kamino.com.br', 'atividades_secundarias': [{'code': '63.19-4-00', 'text': 'Portais, provedores de conteúdo e outros serviços de informação na internet'}, {'code': '63.99-2-00', 'text': 'Outras atividades de prestação de serviços de informação não especificadas anteriormente'}, {'code': '64.63-8-00', 'text': 'Outras sociedades de participação, exceto holdings'}, {'code': '64.91-3-00', 'text': 'Sociedades de fomento mercantil - factoring'}, {'code': '66.13-4-00', 'text': 'Administração de cartões de crédito'}, {'code': '66.19-3-02', 'text': 'Correspondentes de instituições financeiras'}, {'code': '66.19-3-99', 'text': 'Outras atividades auxiliares dos serviços financeiros não especificadas anteriormente'}, {'code': '74.90-1-04', 'text': 'Atividades de intermediação e agenciamento de serviços e negócios em geral, exceto imobiliários'}], 'qsa': [{'nome': 'RODRIGO AFONSO PERENHA', 'qual': '05-Administrador'}, {'nome': 'KAMINO LATAM LLC', 'qual': '37-Sócio Pessoa Jurídica Domiciliado no Exterior', 'pais_origem': 'ESTADOS UNIDOS', 'nome_rep_legal': 'GONZALO PAREJO NAVAJAS', 'qual_rep_legal': '17-Procurador'}, {'nome': 'GUTEMBERG CLAVER DE LIRA FRAGOSO', 'qual': '05-Administrador'}, {'nome': 'GONZALO PAREJO NAVAJAS', 'qual': '05-Administrador'}], 'situacao': 'ATIVA', 'bairro': 'JARDIM PAULISTANO', 'logradouro': 'R CAP ANTONIO ROSA', 'numero': '409', 'cep': '01.443-010', 'municipio': 'SAO PAULO', 'porte': 'DEMAIS', 'natureza_juridica': '206-2 - Sociedade Empresária Limitada', 'uf': 'SP', 'cnpj': '44.270.765/0001-17', 'ultima_atualizacao': '2023-01-24T13:31:03.382Z', 'status': 'OK', 'fantasia': '', 'complemento': '', 'efr': '', 'motivo_situacao': '', 'situacao_especial': '', 'data_situacao_especial': '', 'capital_social': '15994600.00', 'extra': {}, 'billing': {'free': False, 'database': True}}
    id_hubspot = 11236907869

    cnpj = dicionario["cnpj"] # Check
    print(cnpj)
    razao_social = "dicionario['nome']" # Check
    print(razao_social)
    capital_social = dicionario['capital_social'] # Check
    print(capital_social)
    natureza_juridica = dicionario['natureza_juridica'] # Check
    print(natureza_juridica)
    bairro = dicionario['bairro'] # Check
    print(bairro)
    cep = dicionario['cep'] # Check
    print(cep)
    cidade = dicionario['municipio'] # Check
    print(cidade) 
    complemento = dicionario['complemento'] # Check
    print(complemento)
    numero = dicionario['numero'] # Check
    print(numero)
    rua = dicionario['logradouro'] # Check
    print(rua)
    uf = dicionario['uf'] # Check
    print(uf)
    atividade_principal = dicionario["atividade_principal"][0]['text'] # Check
    print(atividade_principal)
    data_abertura = dicionario["abertura"] # Check
    print(data_abertura)
    data_cadastro = dicionario['data_situacao'] # Check
    print(data_cadastro)
    data_ultima_atualizacao = dicionario['ultima_atualizacao'] # Check
    print(data_ultima_atualizacao)

    preenche_cnpj(id_hubspot,dicionario)
