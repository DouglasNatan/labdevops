# -*- coding: utf-8 -*-
from app import app
from labdevops import add
import unittest
#import pytest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()
        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')
    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)
    #def test_conteudo(self):
    #    # verifica o retorno do conteudo da pagina
    #    self.assertEqual(self.result.data.decode('utf-8'), "Eu Amo Minha Família!S2...!")
    def test_deploy():
        assert add(2, 2) == 4

if __name__ == "__main__":
        unittest.main()
