# Percorrendo uma lista
inicio = 0
fim = 100
passo = 10

print(list(range(inicio, fim , passo)))

# Funcionamento da função range. Note que o 10 não é incluído no resultado.
print(list(range(0,10)))

# Ordenando listas.
lista = [10,8,6,3,5,4,1,0,-5,-2]
# sort ordena os números
lista.sort()
print(lista)

# Adiciona elementos no final da lista.
listavazia = []
listavazia.append("Everaldo")
print(listavazia)

# Removendo itens de uma lista
listaRemove = ["a","b", "c", "d", "e" ]
listaRemove.remove("d")
print(listaRemove)

# limpar uma lista
listalimpar = ["python", "Java", "CSS"]
listalimpar.clear()
print(listalimpar)

# Inserir em no final da lista
listainserir = ["Everaldo", "Edson"]
listainserir.insert(1, "Mãe")
print(listainserir)



