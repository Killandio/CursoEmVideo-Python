# Program to count numbers and calculate their sum until a stop condition is met

def main():
    totalNumeros = 0
    totalSoma = 0

    print("Digite números inteiros. Para parar, digite 999.")
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == 999:
                break
            totalNumeros += 1
            totalSoma += numero
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    print(f"\nQuantidade de números digitados: {totalNumeros}")
    print(f"Soma dos números digitados (sem o flag): {totalSoma}")

main()
