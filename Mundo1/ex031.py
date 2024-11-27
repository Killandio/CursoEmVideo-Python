# This program calculates the cost of a trip based on the distance.
# Up to 200 km, the cost is R$0.50 per km. Above 200 km, the cost is R$0.45 per km.

distancia = float(input("Digite a distância da viagem (em km): "))

if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45

print(f"O custo da viagem é R${custo:.2f}.")
