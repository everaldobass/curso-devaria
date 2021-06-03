# Devaria - aula 27 - Python - Aula 2 de linguagem de programação - parte 1

# for
print("\nEstrutura de repetição: ")
for n in range(0,3):
    print(n)

# For com decremento
print("\nEstrutura de repetição Decremento: ")
for n in range(3, 0, -1):
    print(n)

# For para percorrer uma palavra
print("\nEstrutura de repetição percorrer uma palavra: ")

palavra = "Everaldo"
for letra in palavra:
    print(letra)


print("\nEstrutura de repetição percorrendo uma Lista de nomes: ")
nomes = ["Everaldo", "Edson", "Henrique"]
for x in nomes:
    print(x)


print("\nEstrutura de repetição acessar o index dos elementos: ")

carros = ["BMW", "FIAT", "AUDI", "MERCEDRES", "FORD"]
for i, p in enumerate(carros, start=0):
    print(f"carros: {p} no index: {i}")


