from genderbr.servicos.ibge import obter_dados_ibge_nome


def get_gender(nome):

    freq_f = obter_dados_ibge_nome(nome, 'F')
    freq_m = obter_dados_ibge_nome(nome, 'M')

    sum_freq_f = sum(item['frequencia'] for item in freq_f[0]['res'])
    sum_freq_m = sum(item['frequencia'] for item in freq_m[0]['res'])
    return 'F' if sum_freq_f > sum_freq_m else 'M'
