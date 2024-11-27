# This program selects a random name from a list of four student names provided by the user.

from random import *

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)

print(f"O aluno escolhido foi {escolhido}.")
