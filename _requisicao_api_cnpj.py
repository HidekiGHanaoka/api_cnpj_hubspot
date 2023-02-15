import requests

def requisicao_api_cnpj(cnpj: str) -> dict:
    """Retorna todas informações relacionadas a determinado CNPJ

    Args:
        cnpj (str): CNPJ da empresa que deseja obter os dados

    Returns:
        dict: JSON com as informações da empresa
    """

    reqUrl = f"https://receitaws.com.br/v1/cnpj/{cnpj}/days/30"

    headersList = {
    "Authorization": "Bearer token" 
    }

    payload = ""

    return requests.request("GET", reqUrl, data = payload, headers = headersList).json()

if __name__ == "__main__":
    print(requisicao_api_cnpj(44270765000117))