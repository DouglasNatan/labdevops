import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect

#def create_app():
#    app = Flask(__name__)    
#    CSRFProtect(app)  
#    return app    
#    
#@app.route("/")
#def pagina_inicial():
#    return "Eu Amo Minha Família!S2...!"
#    
#if __name__ == '__main__':
#    app = create_app()
#    app.run()

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Eu Amo Minha Família!S2...!"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)