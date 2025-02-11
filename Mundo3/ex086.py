# Program that creates a 3x3 matrix and fills it with values entered by the user.
# At the end, it displays the matrix with the correct formatting.

def main():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for linha in range(3):
        for coluna in range(3):
            matriz[linha][coluna] = getInt(f"Digite um valor para [{linha}, {coluna}]: ")

    print("\nMatriz formatada:")
    for linha in matriz:
        for valor in linha:
            print(f"[{valor:^5}]", end=" ")
        print()  # Line break for matrix formatting

def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

main()
