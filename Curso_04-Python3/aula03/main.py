from aula03.classes.Ave import Ave
from aula03.classes.Reptil import Reptil
from aula03.classes.Mamifero import Mamifero
from aula03.classes.Peixe import Peixe
# Inpute do animal
nome_animal = input("Digite o nome de uma animal: ")

lista_animais = [
    Mamifero("Leão", 4, False, False),
    Reptil("Serpente", 4, True, 0),
    Ave("Gavião", 5000, True, False),
    Peixe("Tubarão",2, True, True)
]

# Verificar se o animal estar na lista
animal_encontrado = list(filter(lambda a : a.nome == nome_animal, lista_animais))

if len(animal_encontrado) == 0:
   print("Animal não encontrado: ")
else:

    try:
     if(isinstance(animal_encontrado[0], Mamifero)):
         print(f"Animal encontrado {animal_encontrado[0].nome} Tipo Mamifero, qtdMamas: {animal_encontrado[0].qtdMamas} ")

     elif (isinstance(animal_encontrado[0], Ave)):
         print(f"Animal encontrado {animal_encontrado[0].nome} Tipo Ave, qtdPenas: {animal_encontrado[0].qtdPenas} ")


     elif(isinstance(animal_encontrado[0], Peixe)):
         print(f"Animal encontrado {animal_encontrado[0].nome} Tipo Peixe, qtdNadadeiras: {animal_encontrado[0].qtdNadadeiras} ")

     elif (isinstance(animal_encontrado[0], Reptil)):
         print(f"Animal encontrado {animal_encontrado[0].nome} Tipo Reptil, qtdPatas: {animal_encontrado[0].qtdPatas} ")

     else:
         print("Ocorreu um erro ao definir o animal: ")

    except Exception as e:
        print("Ocorreu um erro favor tente novamente")



