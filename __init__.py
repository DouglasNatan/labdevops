def add(x, y):
    return x + y

def testRequest():
    # cria uma instância do unittest, precisa do nome "setUp"
    self.app = app.test_client()
    # envia uma requisicao GET para a URL
    self.result = self.app.get('/')