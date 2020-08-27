import responses
from genderbr.genderbr import get_gender


class TestGenderBr():

    @responses.activate
    def test_unit(self):
        resposta_esperada_m = [{"nome": "GUILHERME", "sexo": "M","localidade": "BR","res": [
            {"periodo": "1930[", "frequencia": 1169},
            {"periodo": "[1930,1940[","frequencia": 2383}]}]

        resposta_esperada_f = [{"nome": "GUILHERME", "sexo": "F", "localidade": "BR", "res": [
            {"periodo": "1930[", "frequencia": 1},
            {"periodo": "[1930,1940[", "frequencia": 2}]}]

        responses.add(responses.GET, 'http://servicodados.ibge.gov.br/api/v2/censos/nomes/guilherme?sexo=M',
                      json=resposta_esperada_m, status=200)

        responses.add(responses.GET, 'http://servicodados.ibge.gov.br/api/v2/censos/nomes/guilherme?sexo=F',
                      json=resposta_esperada_f, status=200)

        assert get_gender('guilherme') == 'M'

