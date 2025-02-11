# Program that allows the user to enter five numeric values and inserts them
# directly into the correct position, keeping the list sorted without using sort().

def main():
    lista = []

    for i in range(5):
        numero = getInt("Digite um número: ")

        if i == 0 or numero > lista[-1]:  # Add at the end if it's the largest number
            lista.append(numero)
        else:
            posicao = 0
            while posicao < len(lista):
                if numero <= lista[posicao]:
                    lista.insert(posicao, numero)
                    break
                posicao += 1  # Move to the next position

    print("\nLista ordenada:", lista)


def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")


main()
