# Determines whether a positive integer is a prime number by testing
# divisors up to its square root

def getPosInt(prompt):
    while True:
        try:
            numero = int(input(prompt))
            if numero > 0:
                return numero
            else:
                print("Apenas números inteiros acima de zero são válidos.")
        except ValueError:
            print("Apenas números são válidos.")

numero = getPosInt("Escolha um número para saber se ele é primo: ")

if numero == 1:
    print("O número 1 não é primo.")
elif numero == 2:
    print("O número 2 é primo.")
elif numero % 2 == 0:
    print(f"O número {numero} não pode ser primo, pois é um número par.")
else:
    primo = True
    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
