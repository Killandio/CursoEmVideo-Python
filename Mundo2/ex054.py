# Reads the birth years of seven people, validates the input, and
# counts how many are minors or adults

from datetime import date

anoAtual = date.today().year
maiores = 0
menores = 0

def anoMaxMin(prompt):
    while True:
        try:
            ano = int(input(prompt))
            if ano > anoAtual or ano < 1900:
                print(f"Ano inválido. Digite um ano entre 1900 e {anoAtual}.")
            else:
                return ano
        except ValueError:
            print("Digite apenas números, por favor.")

for i in range(1, 8):
    anoNascimento = anoMaxMin(f"Digite o ano de nascimento da pessoa {i}: ")
    idadePessoas = anoAtual - anoNascimento
    if idadePessoas >= 21:
        maiores += 1
    else:
        menores += 1

print(f"\nNo total, há {maiores} pessoas maiores de idade e {menores} menores de idade.")
