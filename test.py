# -*- coding: utf-8 -*-
from app import app
from labdevops import add
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()
        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')
        self.result1 = self.app.get('/teste')
    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result1.status_code, 200)
    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result1.data.decode('utf-8'), "Fase 5 - Concluída com sucesso!!!")
    def test_request1(self):
        self.assertEqual(self.result.status_code, 200)

if __name__ == "__main__":
        unittest.main()
