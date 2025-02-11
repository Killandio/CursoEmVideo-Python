import random

# Program that helps a player create lottery guesses for the Mega Sena.

def main():
    numCriados = []  # List that will store all the generated guesses
    adicionando = []  # Temporary list to store a single guess
    tentativas = 0

    numPalpites = getInt("Quantos palpites você quer criar? ")

    while tentativas != numPalpites:
        for i in range(6):  # Each guess will have 6 numbers
            numero = random.randint(1, 60)
            adicionando.append(numero)
        numCriados.append(adicionando[:])  # Save a copy of the current guess
        adicionando.clear()  # Clear the temporary list for the next guess
        tentativas += 1

    print("\nPalpites gerados:")
    for i in numCriados:
        print(i)

def getInt(prompt):
    while True:
        try:
            userInput = input(prompt)
            return int(userInput)
        except ValueError:
            print(f"Entrada inválida. Você digitou: {userInput}")

main()
