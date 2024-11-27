# This program reads an integer and checks whether it is even or odd.

numero = input("Digite um número inteiro: ")

if int(numero) >= 0:
    if int(numero) == 0:
        print("O número é par!")
    elif int(numero) % 2 == 0:
        print("O número é par!")
    else:
        print("O número é impar")
else:
    print("Opção inválida!")
