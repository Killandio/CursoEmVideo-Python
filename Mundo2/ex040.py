# Calculates the average of four grades provided by the user.
# Validates input to ensure only positive decimal numbers are accepted.

def main():
    media = calcularMedia()
    print(f"Sua média é {media:.2f}.")

def getPosFloat(prompt):

    while True:
        try:
            numero = float(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Apenas números acima de zero são válidos.")
        except ValueError:
            print("Escolha um número positivo válido para prosseguir!")

def calcularMedia():

    nota1 = getPosFloat("Informe a 1ª nota: ")
    nota2 = getPosFloat("Informe a 2ª nota: ")
    nota3 = getPosFloat("Informe a 3ª nota: ")
    nota4 = getPosFloat("Informe a 4ª nota: ")
    media = (nota1 + nota2 + nota3 + nota4) / 4

    return media

main()
