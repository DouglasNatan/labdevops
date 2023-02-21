def add(x, y):
    return x + y

def validate(a):
    client = app.test_client()
    result = client.get('/')
    return result