# Program that generates five random numbers, stores them in a tuple,
# and displays the list along with the highest and lowest values.

from random import randint

def main():
    numerosAleatorios = (
        randint(1, 100), randint(1, 100), randint(1, 100),
        randint(1, 100), randint(1, 100)
    )

    print("Os números gerados foram:", end=" ")
    for numero in numerosAleatorios:
        print(numero, end=" ")

    menorValor = min(numerosAleatorios)
    maiorValor = max(numerosAleatorios)

    print(f"\nO menor valor sorteado foi {menorValor}")
    print(f"O maior valor sorteado foi {maiorValor}")

main()
