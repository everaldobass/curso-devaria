# Devaria - aula 27 - Python - Aula 2 de linguagem de programação - parte 2
# Listas

try:
    pessoas = []
    nome = ""

    while True:
        nome = input("Digite um nome na lista: ")

        if nome == "Sair":
            break

        pessoas.append(nome)
        print("Pessoas na lista: ")
        print(pessoas)

except Exception as e:
    print("Ocorreu um Erro: ")

