import json
from flask import Blueprint, Response, request
from devaria.aula04.flask.enums.TipoUsuario import TipoUsuario
from devaria.aula04.flask.model.Usuario import Usuario
from devaria.aula04.flask.service.UsuarioService import UsuarioService

usuario_controller = Blueprint('usuario_controller', __name__)


# Declarando uma função
@usuario_controller.route('/login', methods=["POST"])
def login():
    parametros = request.get_json()
    # Mensagem da função
    resposta = {
        "mensagem": ""
    }

    # Estas requisição foi bem sucedida.
    # status_code = 200
    usuario = Usuario(parametros["usuario"], parametros["senha"], TipoUsuario.COMUM.value)

    # Verificar o usuário e senha
    if (usuario.nome == "Everaldo" and usuario.senha == "123"):
        usuario.token = "987654324@123456789"
        # resposta["mensagem"] = "Usuário logado com sucesso!!"
        # Retornando a função
        return Response(json.dumps(usuario.__dict__), status=200, mimetype="application/json")
    else:
        resposta["mensagem"] = "Usuario ou Senha Inválida"
        #  O Cliente deve se autenticar para obter a resposta solicitada.
        # status_code = 401
        # Retornando a função
        return Response(json.dumps(resposta), status=401, mimetype="application/json")


# Função de Consulta de Usuário
@usuario_controller.route('/consultar', methods=["GET"])
def consulta_usuario():
    nome_usuario = request.args.get("nome_usuario")

    resposta_conulta = UsuarioService.consultarUsuario(nome_usuario)

    if (resposta_conulta):
        return Response(json.dumps(resposta_conulta.__dict__), status=401, mimetype="application/json")
    else:
        resposta = {
            "mensagem": "Consultando usuário..."
        }
    return Response(json.dumps(resposta), status=404, mimetype="application/jason")
