# Program to calculate average, maximum, and minimum of user-provided numeros

def main():
    numeros = []
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        escolha = input("Deseja continuar? (s/n): ").strip().lower()
        if escolha != 's':
            break

    if numeros:
        media = sum(numeros) / len(numeros)
        maximoValor = max(numeros)
        minimoValor = min(numeros)

        print(f"\nMédia dos valores: {media}")
        print(f"Maior valor: {maximoValor}")
        print(f"Menor valor: {minimoValor}")
    else:
        print("\nNenhum número foi digitado.")

main()
