# Program that reads multiple numbers and stores them in a list.
# Then, it displays:
# A) How many numbers were entered.
# B) The list of values sorted in descending order.
# C) Whether the number 5 was entered or not.

def main():
    listaNumeros = list()

    while True:
        numero = getInt("Digite um número: ")
        listaNumeros.append(numero)

        continuar = getString("Deseja continuar? [S/N]: ").upper()
        while continuar[0] not in "SN":
            print("Opção inválida! Digite 'S' para continuar ou 'N' para sair.")
            continuar = getString("Deseja continuar? [S/N]: ").upper()

        if continuar[0] == "N":
            break

    print(f"\nQuantidade de números digitados: {len(listaNumeros)}")

    listaNumeros.sort(reverse=True)
    print(f"Lista de valores em ordem decrescente: {listaNumeros}")

    if 5 in listaNumeros:
        print("O número 5 está na lista.")
    else:
        print("O número 5 não foi digitado.")

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
