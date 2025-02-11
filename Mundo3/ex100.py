# Function that generates a list of 5 random numbers and sums the even ones.

import random

def main():
    numeros = []
    sorteia(numeros)
    somaPar(numeros)

def sorteia(lista):
    for _ in range(5):
        lista.append(random.randint(1, 10))
    print(f"Números sorteados: {lista}")

def somaPar(lista):
    soma = sum(num for num in lista if num % 2 == 0)
    print(f"A soma dos números pares é: {soma}")

main()
