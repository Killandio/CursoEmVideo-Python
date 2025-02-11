# Prompts the user for a positive integer and calculates
# its multiplication table from 1 to 10

def getPosInt(prompt):
    while True:
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Apenas números inteiros maiores que zero são permitidos!")
        except ValueError:
            print("Digite apenas números, por favor!")

numero = getPosInt("Digite um número para saber sua tabuada: ")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} vezes {i} é igual a {resultado}")
