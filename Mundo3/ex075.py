# Program that reads four values from the user and stores them in a tuple.
# Then, it displays:
# A) How many times the number 9 appeared.
# B) The position of the first occurrence of the number 3.
# C) The even numbers found in the tuple.

def main():
    numeros = (
        getInt("Digite o 1° número: "),
        getInt("Digite o 2° número: "),
        getInt("Digite o 3° número: "),
        getInt("Digite o 4° número: ")
    )

    print(f"\nOs números digitados foram: {numeros}")

    # Count how many times the number 9 appears
    qtdNove = numeros.count(9)
    print(f"O número 9 apareceu {qtdNove} vezes.")

    # Find the position of the first occurrence of number 3
    if 3 in numeros:
        posicaoTres = numeros.index(3) + 1
        print(f"O primeiro número 3 foi digitado na posição {posicaoTres}.")
    else:
        print("O número 3 não foi digitado.")

    # Find even numbers in the tuple
    print("Os números pares digitados foram:", end=" ")
    hasEven = False
    for num in numeros:
        if num % 2 == 0:
            print(num, end=" ")
            hasEven = True
    if not hasEven:
        print("Nenhum número par foi digitado.")

def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

main()
