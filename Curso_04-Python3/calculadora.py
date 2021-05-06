def soma(n1,n2):
    print(f" Soma: {n1} + {n2}")
    resultado = n1 + n2
    return resultado

def subtracao(n1, n2):
     print(f" Subtraçao: {n1} - {n2}")
     resultado = n1 - n2
     return resultado


def multiplicacao(n1, n2):
    print(f" Multiplicaçao: {n1} * {n2}")
    resultado = n1 * n2
    return resultado


def divisao(n1, n2):
    print(f" Divisao: {n1} / {n2}")
    resultado = n1 / n2
    return resultado


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

operador = input("Digite o operador ")

if operador == '+':
    resultado = soma (n1, n2)
elif operador == '-':
      resultado = subtracao (n1, n2)
elif operador == '*':
      resultado = multiplicacao (n1, n2)
elif operador == '/':
       resultado = divisao (n1, n2)
else:
    print("Operador incorreto: ")

    print(f" Resultado é:  {resultado}" )







