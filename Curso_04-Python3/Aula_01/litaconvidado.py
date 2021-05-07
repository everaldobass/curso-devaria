if __name__ == '__main__':

    listaConvidado = ['Everaldo', 'Edson', 'Eduardo']

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    estaNalista = nome in listaConvidado
    maiorIdade = idade >= 18

    if estaNalista:
        if maiorIdade:
            print("Pode entrar esta convidado: ")
        else:
            print("Seu nome não esta na lista ")

    else:
            print("Seu nome não estar na lista")

