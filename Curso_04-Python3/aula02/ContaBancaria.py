# Definição de uma Classe
class ContaBancaria:

    def __init__(self, tipo, conta, agencia):
        self.tipo = tipo
        self.conta = conta
        self.agencia = agencia

    # Métodos / Ações
    def exibirDadosConta(self):
            print(f"Conta criada Tipo: {conta1.tipo} - Conta: {conta1.conta} - Agência: {conta1.agencia}")


# Instanciando uma Conta em Python
conta1 = ContaBancaria("Corrente", 6584, "578658")
conta1.exibirDadosConta()


