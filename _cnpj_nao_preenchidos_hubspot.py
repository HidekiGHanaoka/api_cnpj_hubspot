import requests
import json

def cnpj_nao_preenchidos_hubspot() -> list:
    """Busca no HubSpot todas empresas que tem CNPJ e suas informações relacionadas a ele não estão preenchidas ainda e retorna uma lista com todas elas

    Returns:
        list: lista de tuplas, em que cada tupla tem o ID HubSpot da empresa e seu CNPJ
    """
    reqUrl = "https://api.hubapi.com/crm/v3/objects/companies/search"
    proxima_pagina = 0
    empresas_nao_preenchidas = []
    headersList = {
        "Authorization": "Bearer token",
        "Content-Type": "application/json" 
        }

    while proxima_pagina != None:

        payload = json.dumps({
            "properties" : ["cnpj"],
            "filterGroups":[{
                "filters": [
                    {
                        "propertyName": "cnpj",
                        "operator": "HAS_PROPERTY"
                    },
                    {
                    "propertyName": "data_eleicao_diretoria_da_empresa_brasil",
                    "operator": "NOT_HAS_PROPERTY"
                    }]
                }],
            "after" : f"{proxima_pagina}"
        })

        dicionario: dict = requests.request("POST", reqUrl, data = payload,  headers = headersList).json()

        proxima_pagina = None

        for index, objeto in dicionario.items():

            if index == "paging":
                proxima_pagina = objeto["next"]["after"]

            elif index == "results":
                for empresa in objeto:
                    empresas_nao_preenchidas.append([empresa["id"], empresa["properties"]["cnpj"]])

    return empresas_nao_preenchidas

if __name__ == "__main__":
    print(cnpj_nao_preenchidos_hubspot())