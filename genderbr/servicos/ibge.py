import requests


def obter_dados_ibge_nome(nome, sexo):
    response = requests.get('http://servicodados.ibge.gov.br/api/v2/censos/nomes/' + nome + '?sexo=' + sexo)
    return response.json()
