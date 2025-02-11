# Reads integers until a stop condition and calculates
# the total count and sum.

def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Apenas números inteiros são permitidos.")

quantidade = 0
somaTotal = 0

while True:
    numero = getInt("Digite um número inteiro (999 para parar): ")
    if numero == 999:
        break
    quantidade += 1
    somaTotal += numero

print(f"Você digitou {quantidade} números e a soma entre eles foi {somaTotal}.")
