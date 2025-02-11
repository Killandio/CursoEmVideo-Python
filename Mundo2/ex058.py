# The computer chooses a number between 0 and 10, and the player must guess it.
# Counts attempts until correct.

import random

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite apenas números inteiros, por favor.")

numeroComputador = random.randint(0, 10)
tentativas = 0
acertou = False

print("O computador pensou em um número entre 0 e 10. Tente adivinhar!")

while not acertou:
    palpite = getInt("Qual é o seu palpite? ")
    tentativas += 1
    if palpite == numeroComputador:
        acertou = True
        print(f"Parabéns! Você acertou o número {numeroComputador} com {tentativas} tentativa(s).")
    elif palpite < numeroComputador:
        print("Mais... Tente um número maior.")
    else:
        print("Menos... Tente um número menor.")
