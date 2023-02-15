# 🪢Integração de [API de CNPJ](https://developers.receitaws.com.br/#/) com HubSpot

* O programa busca nas empresas cadastradas no HubSpot da Kamino quais tem CNPJ cadastrados e ainda não foram preenchidas com as informações relacionadas a ele, faz uma requisição para a API do CNPJ e preenche informações referentes a empresa no HubSpot (Ex: Capital Social, Razão Social, Natureza Jurídica, Endereço, Data de fundação).
* A main realiza todo o processo, importando as funções auxiliares.
