from aula03.classes.Animal import Animal

class Reptil(Animal):
    def __init__(self, nome, temperaturaCoporal, isRepetilTerrestre, qtdPatas):
        super().__init__(nome)
        self.temperaturaCoporal = temperaturaCoporal
        self.isRepetilTerrestre = isRepetilTerrestre
        self.qtdPatas = qtdPatas
