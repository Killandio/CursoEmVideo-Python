# Program that reads the name and weight of multiple people and stores them in a list.
# Then, it displays:
# A) The number of people registered.
# B) A list of the heaviest people.
# C) A list of the lightest people.

def main():
    listaPessoas = list()
    maiorPeso = menorPeso = 0

    while True:
        nome = getString("Digite o nome da pessoa: ")
        peso = getFloat("Digite o peso da pessoa (kg): ")

        pessoa = [nome, peso]
        listaPessoas.append(pessoa)

        if len(listaPessoas) == 1:
            maiorPeso = menorPeso = peso
        else:
            if peso > maiorPeso:
                maiorPeso = peso
            if peso < menorPeso:
                menorPeso = peso

        continuar = getString("Deseja continuar? [S/N]: ").upper()
        while continuar[0] not in "SN":
            print("Opção inválida! Digite 'S' para continuar ou 'N' para sair.")
            continuar = getString("Deseja continuar? [S/N]: ").upper()

        if continuar[0] == "N":
            break

    print(f"\nNúmero total de pessoas cadastradas: {len(listaPessoas)}")

    print(f"\nPessoas mais pesadas ({maiorPeso} kg): ", end="")
    for pessoa in listaPessoas:
        if pessoa[1] == maiorPeso:
            print(f"[{pessoa[0]}]", end=" ")

    print(f"\nPessoas mais leves ({menorPeso} kg): ", end="")
    for pessoa in listaPessoas:
        if pessoa[1] == menorPeso:
            print(f"[{pessoa[0]}]", end=" ")

    print()

def getString(prompt):
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        else:
            print("Entrada inválida. Insira uma string não vazia.")

def getFloat(prompt):
    while True:
        try:
            userInput = input(prompt)
            return float(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

main()
