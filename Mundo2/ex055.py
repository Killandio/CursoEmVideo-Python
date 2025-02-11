# Reads the weight of five people and determines
# the highest and lowest weight

def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Digite apenas números válidos para o peso.")

maior = 0
menor = 0

for i in range(1, 6):
    peso = getFloat(f"Digite o peso da {i}ª pessoa (em kg): ")
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso digitado foi {maior:.2f} kg.")
print(f"O menor peso digitado foi {menor:.2f} kg.")
