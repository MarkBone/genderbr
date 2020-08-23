import pytest


class TestGenderBr():

    def test_true(self, mocker):
        from genderbr.genderbr import GenderBr
        GenderBr()
        assert True
