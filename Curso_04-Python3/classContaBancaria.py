# Declarando uma classe
class ContaBancaria:
    def __init__(self, tipo, conta, agencia ):
        self.tipo = tipo
        self.conta = conta
        self.agencia = agencia

    # Função que exibe os dados da conta
    def exibirDadosDaConta(self):
         print(f"\nTipo: {self.tipo} - Conta:{self.conta} - Agencia: {self.agencia}")



if __name__ == "__main__":
        # Instanciando as contas
        conta1 = ContaBancaria("corrente", 65878, "57002")
        conta1.exibirDadosDaConta()
        
        conta2 = ContaBancaria("poupança", 879879, "25689")
        conta2.exibirDadosDaConta()
        