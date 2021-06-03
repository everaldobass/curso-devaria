# Devaria - aula 27 - Python - Aula 2 de linguagem de programação - parte 1
print("\nWhile Crescente")
n = 0
while n < 5:
    print(n)
    n = n + 1

print("\nWhile Desafio utilizando função")
# Função Lavar Carro
def lavarCarro(posicao):
    print(f"Lavando o Carro {posicao}")

# Função Verificar
def Verificar(posicao):
    if(posicao > 5):
        return False
    else:
        return True


temCarroNaFila = True
posicao = 1
while temCarroNaFila:
    lavarCarro(posicao)
    posicao += 1
    temCarroNaFila = Verificar(posicao)
else:
    print("Terminou de Lavar os carros")






