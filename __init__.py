def add(x, y):
    return x + y

def app(app):
    client = app.test_client()
    result = client.get('/')
    return result