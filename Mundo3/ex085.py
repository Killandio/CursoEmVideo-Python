# Program that allows the user to enter seven numeric values and stores them in a single list.
# The list keeps even and odd numbers separated.
# At the end, both even and odd numbers are displayed in ascending order.

def main():
    listaNumeros = [[], []]  # Index 0 for even numbers, index 1 for odd numbers

    for i in range(7):
        numero = getInt(f"Digite o {i+1}° número: ")

        if numero % 2 == 0:
            listaNumeros[0].append(numero)  # Store even numbers at index 0
        else:
            listaNumeros[1].append(numero)  # Store odd numbers at index 1

    listaNumeros[0].sort()
    listaNumeros[1].sort()

    print(f"\nNúmeros pares em ordem crescente: {listaNumeros[0]}")
    print(f"Números ímpares em ordem crescente: {listaNumeros[1]}")

def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

main()
