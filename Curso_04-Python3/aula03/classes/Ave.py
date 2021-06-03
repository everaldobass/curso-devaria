from aula03.classes.Animal import Animal


class Ave(Animal):
    def __init__(self, nome, qtdPenas, consegueVoar, consegueMigrar):
        # Atributos da Classe animal
        super().__init__(nome)
        # Atributos da classe AVE
        self.qtdPenas = qtdPenas
        self.consegueVoar = consegueVoar
        self.consegueMigrar = consegueMigrar
