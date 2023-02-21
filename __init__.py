from labdevops import app as flask_app

def add(x, y):
    return x + y

def app():
    yield flask_app

def client(app):
    return app.test_client()