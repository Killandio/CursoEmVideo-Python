# Determines a person's military enlistment status based on their year of
# birth, indicating if they need to enlist, have time left, or are overdue.


def getPosInt(prompt):
    while True:
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Apenas números inteiros acima de zero são válidos")
        except ValueError:
            print("Escolha um número inteiro para conseguir prosseguir!")

from datetime import date
dataAtual = date.today().year
dataNascimento = getPosInt("Informe a sua data de nascimento: ")

idade = dataAtual - dataNascimento
alistamento = dataNascimento + idade
atrasado = dataAtual - (idade - 18)

if idade < 18:
    print(f"Você tem apenas {idade} anos, ainda não está na hora de servir. Você deverá se apresentar para servir apenas em {alistamento}.")
elif idade == 18:
    print(f"Você já tem 18 anos. Está na hora de servir!")
else:
    print(f"Você tem {idade} anos. Já passou da hora de servir. Você deveria ter servido em {atrasado}")