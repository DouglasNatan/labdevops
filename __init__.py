from app import app

def add(x, y):
    return x + y

def app():
    client = app.test_client()
    result = client.get('/')
    return result