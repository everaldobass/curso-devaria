import json
from flask import Flask
from devaria.aula04.flask.controllers.UsuarioController import usuario_controller

app = Flask(__name__)
# Instanciou
app.register_blueprint(usuario_controller, url_prefix='/api/v1/usuario' )

if __name__ == '__main__':
    # Subindo o Servidor
    app.run(host="127.0.0.1", port=3000)

















# Primeiro Exemplo utilizado
"""
@app.route('/api/v1/hello', methods=["GET"])
def hello():
    retornoApi = {
        "mensagem":"Aplicação com Jason, primeira API em Python"

    }

    return Response(json.dumps(retornoApi), mimetype="application/jason")
"""