# This program compares two integers input by the user and determines
# whether the first number is greater, the second one is greater,
# or if they are equal.

while True:
    try:
        primeiroNumero = int(input("Digite o primeiro número inteiro: "))
        segundoNumero = int(input("Digite o segundo número inteiro: "))

        if primeiroNumero > segundoNumero:
            print(f"O número {primeiroNumero} é maior que o número {segundoNumero}.")
        elif segundoNumero > primeiroNumero:
            print(f"O número {segundoNumero} é maior que o número {primeiroNumero}.")
        else:
            print("Os dois números são iguais.")
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")
