# Program that reads multiple numbers and stores them in a list.
# Then, it creates two additional lists:
# - One containing only even numbers.
# - One containing only odd numbers.
# Finally, it displays the contents of all three lists.

def main():
    listaNumeros = list()
    listaPares = list()
    listaImpares = list()

    while True:
        numero = getInt("Digite um número: ")
        listaNumeros.append(numero)

        if numero % 2 == 0:
            listaPares.append(numero)
        else:
            listaImpares.append(numero)

        continuar = getString("Deseja continuar? [S/N]: ").upper()
        while continuar[0] not in "SN":
            print("Opção inválida! Digite 'S' para continuar ou 'N' para sair.")
            continuar = getString("Deseja continuar? [S/N]: ").upper()

        if continuar[0] == "N":
            break

    print(f"\nLista completa: {listaNumeros}")
    print(f"Lista de números pares: {listaPares}")
    print(f"Lista de números ímpares: {listaImpares}")

def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Insira uma string não vazia.")

main()
