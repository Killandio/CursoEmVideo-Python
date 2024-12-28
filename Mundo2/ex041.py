# Classifies athletes into categories based on their age.
# Ensures valid inputs for both the athlete's name and age.

def getPosInt(prompt):

    while True:
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Apenas números acima de zero são válidos.")
        except ValueError:
            print("Escolha um número positivo válido para prosseguir!")

def getString(prompt):

    while True:
        entrada = input(prompt)
        if entrada.isalpha():
            return entrada
        else:
            print("Digite apenas letras!")

nomeAtleta = getString("Digite o nome do atleta: ")
idadeAtleta = getPosInt("Digite a idade do atleta: ")

if idadeAtleta < 10:
    categoria = "MIRIM"
elif idadeAtleta < 15:
    categoria = "INFANTIL"
elif idadeAtleta < 20:
    categoria = "JUNIOR"
elif idadeAtleta < 26:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

print(f"O atleta {nomeAtleta} pertence à categoria {categoria}.")
