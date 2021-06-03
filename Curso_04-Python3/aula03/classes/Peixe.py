from aula03.classes.Animal import Animal
# Definição da classe Peixe
class Peixe(Animal):
    def __init__(self, nome, qtdNadadeiras, isPeixeAguaSalgada, isCarnivero):

        # Herda atributo da classe animal
        super().__init__(nome)

        # Atributos da classe peixe
        self.qtdNadadeiras = qtdNadadeiras
        self.isPeixeAguaSalgada = isPeixeAguaSalgada
        self.isCarnivero = isCarnivero