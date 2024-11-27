# This program generates a random number between 0 and 5 and asks the user to guess it.

from random import randint

numeroAleatorio = randint(0, 5)
palpite = int(input("Tente adivinhar o número entre 0 e 5: "))

acertou = palpite == numeroAleatorio

print(f"O número era {numeroAleatorio}. Você acertou? {acertou}")
