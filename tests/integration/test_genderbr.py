from genderbr.genderbr import get_gender


class TestGenderBr():

    def test_gender(self):
        assert get_gender('maria') == 'F'
        assert get_gender('joao') == 'M'
        assert get_gender('mario') == 'M'
        assert get_gender('teresa') == 'F'
        assert get_gender('filipe') == 'M'
