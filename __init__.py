from flask import Flask
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    
    csrf = CSRFProtect(app)  
    
    @app.route("/")
    def pagina_inicial():
        return "Eu Amo Minha Família!S2...!"

    return app    

    def add(x, y):
    return x + y 
    
if __name__ == '__main__':
    app = create_app()
    app.run()

