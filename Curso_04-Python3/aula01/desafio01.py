# Devaria aula 23 Python Aula 1 de linguagem de programação parte 4

# Inpute do usuário
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o Segundo número: "))
operador = input("\nDigite o Operador do Calculo: ")

res = None

# Declarando as funções
def soma(n1, n2):
    print(f"Somando {n1} + {n2}")
    res = n1 + n2
    return res

def subtracao(n1 , n2):
    print(f"Subtração {n1} - {n2}")
    res = n1 - n2
    return res

def multiplicacao(n1, n2):
    print(f"Multiplicação {n1} * {n2}")
    res = n1 * n2
    return res

def divisao(n1, n2):
    print(f"Divisão {n1} / {n2}")
    res = n1 / n2
    return res

# Inserindo o operado matemático
if operador == "+":
    res = soma(n1,n2)
elif operador == "-":
    res = subtracao(n1,n2)
elif operador == "*":
    res = multiplicacao(n1,n2)
elif operador == "/":
    res = divisao(n1,n2)
else:
    print("Operador errado: ")

# Mostra o Resultado na Tela
print(f"Resultado da operação é : {res}")

