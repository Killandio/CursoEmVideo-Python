# Displays the first 10 terms of an arithmetic progression based on
# user input.

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Apenas números inteiros são permitidos.")

primeiroTermo = getInt("Digite o primeiro termo da PA: ")
razao = getInt("Digite a razão da PA: ")

termo = primeiroTermo
contador = 1

while contador <= 10:
    print(f"{termo}", end=" -> " if contador < 10 else " -> FIM\n")
    termo += razao  # Calculate the next term
    contador += 1
