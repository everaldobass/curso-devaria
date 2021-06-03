# Devaria - aula 27 - Python - Aula 2 de linguagem de programação - parte 2
# Funções Anônimas

# Calculando média com lambda Funções anonimas
alunonotas =[50, 60, 30, 20, 10]
medianotas = lambda notas : sum(notas) / len(notas)
print(medianotas(alunonotas))

# Calculando com filtros
notasAlunos =[50, 60, 30, 20, 10, 90, 100, 40, 30, 70]
notasfiltradas = list(filter(lambda nota : nota <= 80, notasAlunos) )
print(notasfiltradas)

