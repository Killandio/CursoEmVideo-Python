# Calculates and displays the factorial of a number with step-by-step
# multiplication breakdown.

def main():
    fatorial()


def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Apenas números inteiros são permitidos")

def fatorial():
    numero = getInt("Digite um número para saber seu fatorial: ")
    inicial = numero
    fatorial = 1
    while inicial > 0:
        print(f"{inicial}", end="")
        print(" x " if inicial > 1 else " = ",end="")
        fatorial *= inicial
        inicial -= 1
    print(f"{fatorial}")
main()