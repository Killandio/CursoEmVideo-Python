# Reads six integers from the user and sums only the even numbers

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite apenas números inteiros, por favor!")

soma = 0
for i in range(6):
    numero = getInt(f"Digite o {i+1}º número inteiro: ")
    if numero % 2 == 0:
        soma += numero

print(f"A soma dos números pares digitados é: {soma}")
