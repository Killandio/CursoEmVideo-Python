# Function that counts from start to end with a given step.

import time


def main():
    print("\nContagem de 1 até 10 de 1 em 1:")
    contador(1, 10, 1)

    print("\nContagem de 10 até 0 de 2 em 2:")
    contador(10, 0, -2)

    print("\nContagem personalizada:")
    inicio = getInt("Início: ")
    fim = getInt("Fim: ")
    passo = getInt("Passo: ")
    contador(inicio, fim, passo)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1 if inicio < fim else -1
    elif passo < 0 and inicio < fim:
        passo = abs(passo)

    print(f"Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:")

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ", flush=True)
            time.sleep(0.5)
    else:
        for i in range(inicio, fim - 1, passo):
            print(i, end=" ", flush=True)
            time.sleep(0.5)

    print("FIM!")


def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")


main()
