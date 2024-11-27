# This program randomly shuffles the order of a list of four student names provided by the user.

from random import shuffle

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)

print("A ordem de apresentação será:")
for aluno in alunos:
    print(aluno)
