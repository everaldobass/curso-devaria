# Devaria aula 23 Python Aula 1 de linguagem de programação parte 4

def Validar(valido1, valido2):

    if valido1 and valido2:
        return "As duas variaveis verdadeiras"
    else:
        return "Variaveis do valor é Falso"

if __name__ == '__name__':
    teste1 = True
    teste2 = False

    respostaFuncao = Validar(teste1, teste2)
    print(respostaFuncao)

