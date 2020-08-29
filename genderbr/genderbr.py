from genderbr.servicos.ibge import obter_dados_ibge_nome


def get_gender(nome):

    freq_f = obter_dados_ibge_nome(nome, 'F')
    freq_m = obter_dados_ibge_nome(nome, 'M')

    if freq_f:
        sum_freq_f = sum(item['frequencia'] for item in freq_f[0]['res'])
    else:
        sum_freq_f = 0

    if freq_m:
        sum_freq_m = sum(item['frequencia'] for item in freq_m[0]['res'])
    else:
        sum_freq_m = 0

    if sum_freq_f > 0 or sum_freq_m > 0:
        return 'F' if sum_freq_f > sum_freq_m else 'M'
    else:
        return None
