from aula03.classes.Animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, qtdMamas, isMamiferoAquatico, botaOvo ):
        super().__init__(nome)

        self.qtdMamas = qtdMamas
        self.isMamiferoAquatico = isMamiferoAquatico
        self.botaOvo = botaOvo