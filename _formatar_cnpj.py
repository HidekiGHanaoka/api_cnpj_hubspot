def formatar_cnpj(cnpj: str) -> str:
    """Recebe um cnpj em string com "/", "." e "-" e as remove, deixando apenas os números e retornando um inteiro

    Args:
        cnpj (str): String do cnpj

    Returns:
        str: Inteiro com apenas os número do cnpj
    """    
    cnpj = cnpj.replace(".", "")
    cnpj = cnpj.replace("/", "")
    return cnpj.replace("-", "")

if __name__ == "__main__":
    cnpj = "44.270.765/0001-17"
    esperado = "44270765000117"
    if formatar_cnpj(cnpj) == esperado:
        print("Teste OK!")
    else:
        print("Erro")
