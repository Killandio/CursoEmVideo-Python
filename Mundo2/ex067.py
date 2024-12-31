# Program to Display Multiplication Table Until Negative Input

def main():
    while True:
        numero = int(input("Digite um número para ver sua tabuada (número negativo para parar): "))
        if numero < 0:
            break
        print(f"Tabuada de {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
        print()

main()
