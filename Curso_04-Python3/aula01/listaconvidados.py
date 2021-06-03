listaConvidados = ['Everaldo', 'Edson', 'Eduardo', 'Elias']

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Verficar se estar na lista
estaNaLista = nome in listaConvidados
# Verificar a idade
maiorIdade = idade >= 18

if estaNaLista and maiorIdade:
    if maiorIdade:
        print("Pode entrar seu nome estar na lista: ")
    else:
        print("Seu nome estar na lista e não é maior idade: ")
else:
    print("Seu nome não estar na lista e você não é maior idade: ")