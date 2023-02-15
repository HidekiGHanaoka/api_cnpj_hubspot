from _cnpj_nao_preenchidos_hubspot import cnpj_nao_preenchidos_hubspot
from _formatar_cnpj import formatar_cnpj
from _requisicao_api_cnpj import requisicao_api_cnpj
from _preenche_cnpj import preenche_cnpj

lista_empresas_nao_preenchidas = cnpj_nao_preenchidos_hubspot()
for empresa in lista_empresas_nao_preenchidas:
    try:
        cnpj_formatado = formatar_cnpj(empresa[1])
        dicionario = requisicao_api_cnpj(cnpj_formatado)
        preenche_cnpj(empresa[0], dicionario)
        print(f"ID: {empresa} preenchido")
    except Exception:
        print(f"Erro na empresa {empresa}")
        continue