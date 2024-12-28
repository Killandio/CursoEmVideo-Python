# Converts a positive integer to binary, octal, or hexadecimal
# based on user choice.

def getPosInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
numero = getPosInt("Digite um número: ")
escolha = -1
while escolha != 4:
    print("Converter para\n 1) Binário\n 2) Octal\n 3) Hexadecimal\n 4) Sair\n")
    escolha = getPosInt("Digite o número correspondente a opção que deseja acessar: ")
    if escolha == 1:
        binario = format(numero,'b')
        print(f"Binário: {binario}")
    elif escolha == 2:
        octal = format(numero,'o')
        print(f"Octal: {octal}")
    elif escolha == 3:
        hexadecimal = format(numero,'X')
        print(f"Hexadecimal: {hexadecimal}")
    elif escolha >= 5 or escolha <= 0:
        print("Opção inválida, tente novamente.")