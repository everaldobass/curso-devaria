#Devaria - aula 23 - Python - Aula 1 de linguagem de programação - parte 3

# Operador OR
def SecondOperador():
    print("Avaliando o segundo operador.")
    return True

# Falso e Verdadeiro = Verdadeiro
a = False or SecondOperador()
print(a)

# Verdadeiro e Verdadeiro = Verdadeiro
b = True or SecondOperador()
print(b)