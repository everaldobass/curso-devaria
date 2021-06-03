from devaria.aula04.flask.enums.TipoUsuario import TipoUsuario
from devaria.aula04.flask.model.Usuario import Usuario

class UsuarioService:

    def __init__(self):
        pass

    def consultarUsuario(self, nomeUsuario):
        lista_usuario = [
            Usuario( "Everaldo", "123", TipoUsuario.COMUM.value),
            Usuario("Edson", "1234", TipoUsuario.COMUM.value),
            Usuario("Elias", "12345", TipoUsuario.COMUM.value),
            Usuario("Eriberto", "123456", TipoUsuario.COMUM.value),
        ]

        for usuarioLista in lista_usuario:
            if (usuarioLista.nome  == nomeUsuario ):
                return usuarioLista

            return none