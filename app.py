from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Eu Amo Minha Família!"

if __name__ == '__main__':
    app.run()