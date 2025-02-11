# Program that enhances the previous 3x3 matrix challenge.
# At the end, it displays:
# A) The sum of all even values entered.
# B) The sum of the values in the third column.
# C) The largest value in the second row.

def main():
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    somaPares = somaTerceiraColuna = maiorSegundaLinha = 0

    for linha in range(3):
        for coluna in range(3):
            matriz[linha][coluna] = getInt(f"Digite um valor para [{linha}, {coluna}]: ")

            # Check for even numbers
            if matriz[linha][coluna] % 2 == 0:
                somaPares += matriz[linha][coluna]

            # Sum values in the third column
            if coluna == 2:
                somaTerceiraColuna += matriz[linha][coluna]

    # Find the largest value in the second row
    maiorSegundaLinha = max(matriz[1])

    # Display the formatted matrix
    print("\nMatriz formatada:")
    for linha in matriz:
        for valor in linha:
            print(f"[{valor:^5}]", end=" ")
        print()  # Line break for matrix formatting

    # Display results
    print(f"\nA soma de todos os valores pares é: {somaPares}")
    print(f"A soma dos valores da terceira coluna é: {somaTerceiraColuna}")
    print(f"O maior valor da segunda linha é: {maiorSegundaLinha}")


def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")


main()
