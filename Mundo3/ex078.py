# Program that reads 5 numeric values from the user and stores them in a list.
# Then, it displays the highest and lowest values along with their respective positions in the list.

def main():
    listaNumeros = list()

    # Read 5 integer values from the user
    for i in range(5):
        numero = getInt("Escolha um número inteiro: ")
        listaNumeros.append(numero)

    maiorValor = max(listaNumeros)
    menorValor = min(listaNumeros)

    print(f"\nO maior valor digitado foi {maiorValor} na posição:", end=" ")
    for i, valor in enumerate(listaNumeros):
        if valor == maiorValor:
            print(i, end=" ")

    print(f"\nO menor valor digitado foi {menorValor} na posição:", end=" ")
    for i, valor in enumerate(listaNumeros):
        if valor == menorValor:
            print(i, end=" ")

    print()

def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

main()
