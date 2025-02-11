# Program that allows the user to enter multiple numeric values into a list.
# If a number is already in the list, it will not be added.
# At the end, the unique values are displayed in ascending order.

def main():
    listaNumeros = list()

    while True:
        numero = getInt("Digite um número: ")

        if numero not in listaNumeros:
            listaNumeros.append(numero)
            print("Número adicionado com sucesso.")
        else:
            print("Número já existe na lista. Não será adicionado.")

        continuar = getString("Deseja continuar? [S/N]: ").upper()
        while continuar[0] not in "SN":
            print("Opção inválida! Digite 'S' para continuar ou 'N' para sair.")
            continuar = getString("Deseja continuar? [S/N]: ").upper()

        if continuar[0] == "N":
            break

    listaNumeros.sort()

    print("\nOs valores únicos digitados, em ordem crescente, são:")
    for num in listaNumeros:
        print(num, end=" ")

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
